'''
This module contains the necessary functionality to run
basic runtime tests. The test suite is run for all programming
languages added in `test/config.py`.

**Important**: This test suite makes several assumptions regarding
naming conventions and the location of specific files:

  - The bot binary should be located at
    `docker-sandbox/test/bot_binaries/<lowercase_programming_language_name>/`
  - The compiler image should be named as
    `gcr.io/riddles-microservices/sandbox-runtime-<lowercase_programming_language_name>`

A marker is generated for each programming language added to the
test suite. This marker can be used to run a subset of the tests.
See README.md for more info.
'''
import os
import pytest
import shutil

from test.config import PROGRAMMING_LANGUAGES
from util.subprocess import SubprocessRunner
from util.temp_dir import temp_dir
from util.test_utils import (
    as_id,
    as_param,
    create_docker_compile_command,
    create_docker_runtime_command,
    compiler_image,
    get_manifest_executable,
    runtime_image,
)

@pytest.fixture(
    ids=as_id,
    params=list(map(as_param, PROGRAMMING_LANGUAGES)),
    scope="module",
)
def runtime(request):
    programming_language, runtime = request.param

    module_dir = os.path.dirname(os.path.realpath(__file__))
    bin_dir = os.path.join(
        module_dir,
        'bot_binaries/{}'.format(programming_language)
    )
    manifest_path = os.path.join(bin_dir, 'manifest')

    # Step 1: Run the runtime and get the output
    command = create_docker_runtime_command(
        bin_dir,
        runtime,
        get_manifest_executable(manifest_path),
        runtime_image(programming_language)
    )
    result = SubprocessRunner().run('cat test_scenario.txt | ' + command)

    if (result.return_code != 0):
        print('===STDOUT===')
        print(result.stdout)
        print('===STDERR===')
        print(result.stderr)

    return result

@pytest.mark.runtime
def test_succesful_return_code(runtime):
    assert runtime.return_code == 0

@pytest.mark.runtime
def test_bot_returns_correct_output(runtime):
    assert runtime.stdout.strip() in ['rock', 'paper', 'scissors']
