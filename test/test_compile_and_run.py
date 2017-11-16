'''
This module contains the necessary functionality to run
basic compiler tests. In order to add a test for a specific
compiler, add a tuple with the lowercase name of the programming
language and the filename of the bot source code to the FIXTURES
list.

For example, to add a test for the python compiler, add the
following:

```
FIXTURES = [
    ...
    ('python', 'basic_bot.py'),
    ...
]
```

**Important**: This test suite makes several assumptions regarding
naming conventions and the location of specific files:

  - The bot source code should be located at
    `docker-sandbox/test/bot_sources/<lowercase_programming_language_name>/`
  - The compiler image should be named as
    `gcr.io/riddles-microservices/sandbox-compiler-<lowercase_programming_language_name>`

A marker is generated for each programming language added to the
test suite. This marker can be used to run a subset of the tests.
See README.md for more info.
'''
import os
import pytest
import shutil
from contextlib import contextmanager

from util.subprocess import SubprocessRunner
from util.temp_dir import temp_dir
from util.test_utils import create_docker_compile_command
from util.test_utils import create_docker_runtime_command
from util.test_utils import compiler_image
from util.test_utils import get_manifest_executable
from util.test_utils import runtime_image

FIXTURES = [
    'javascript',
    'php',
]

def as_id(datum):
    # Important:
    # 
    # This function cannot return a value which is also
    # used as a marker. This screws up the test selection
    # for some reason.
    return 'ProgrammingLanguage(slug={})'.format(datum)

def as_param(datum):
    # Dynamically create a marker from fixture data,
    # so it becomes possible to run the compiler tests
    # for a subset of programming languages.
    mark = getattr(pytest.mark, datum)
    return pytest.param(datum, marks=mark)

@pytest.fixture(
    ids=as_id,
    params=list(map(as_param, FIXTURES)),
    scope="module",
)
def compiler_setup(request):
    programming_language = request.param
    module_dir = os.path.dirname(os.path.realpath(__file__))

    # Note: all temp dirs should be created within `/tmp` instead of `/var`
    # as macOS cannot volume mount folders located in `/var` by default.
    # See https://docs.docker.com/docker-for-mac/osxfs/#namespaces for more
    # info.
    with temp_dir(dir='/tmp') as path:

        # Step 1: Create the required folder structure
        source_dir = os.path.join(path, 'source')
        bin_dir = os.path.join(path, 'bin')

        os.mkdir(bin_dir)

        shutil.copytree(
            os.path.join(module_dir, 'bot_sources/{}'.format(programming_language)),
            source_dir
        )

        # Step 2: Run the compiler and get the output
        command = create_docker_compile_command(
            source_dir,
            bin_dir,
            compiler_image(programming_language)
        )
        result = SubprocessRunner().run(command)

        if (result.return_code != 0):
            print('===STDOUT===')
            print(result.stdout)
            print('===STDERR===')
            print(result.stderr)

        yield bin_dir, result

@pytest.fixture(
    ids=as_id,
    params=list(map(as_param, FIXTURES)),
    scope="module",
)
def runtime_result(compiler_setup, request, update_binaries):
    bin_dir, result = compiler_setup
    programming_language = request.param[0]
    module_dir = os.path.dirname(os.path.realpath(__file__))
    manifest_path = os.path.join(bin_dir, 'manifest')

    # Step 0: Update the bot binaries if the `--update-binaries` flag is passed
    if result.return_code == 0 and update_binaries:
        shutil.copytree(
            bin_dir,
            os.path.join(module_dir, 'bot_binaries/{}'.format(programming_language))
        )

    # Step 1: Run the runtime and get the output
    command = create_docker_runtime_command(
        bin_dir,
        get_manifest_executable(
            manifest_path,
            bin_dir,
        ),
        runtime_image(programming_language)
    )
    result = SubprocessRunner().run('cat test_scenario.txt | ' + command)

    if (result.return_code != 0):
        print('===STDOUT===')
        print(result.stdout)
        print('===STDERR===')
        print(result.stderr)

    return result

@pytest.mark.compiler
def test_succesful_return_code(runtime_result):
    assert runtime_result.return_code == 0

def test_bot_returns_correct_output(runtime_result):
    assert runtime_result.stdout.strip() in ['rock', 'paper', 'scissors']
