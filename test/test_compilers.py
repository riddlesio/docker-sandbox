'''
This module contains the necessary functionality to run
basic compiler tests.

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
    autouse=True,
    ids=as_id,
    params=list(map(as_param, PROGRAMMING_LANGUAGES)),
    scope="module",
)
def compile_result(request, update_binaries):
    programming_language, runtime = request.param
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

        if result.return_code != 0:
            print('===STDOUT===')
            print(result.stdout)
            print('===STDERR===')
            print(result.stderr)
        elif update_binaries:
            binary_dir = os.path.join(
                module_dir,
                'bot_binaries/{}'.format(programming_language)
            )
            
            if (os.path.exists(binary_dir)):
                shutil.rmtree(binary_dir)
            shutil.copytree(bin_dir, binary_dir)

        yield bin_dir, result, programming_language, runtime


@pytest.fixture(scope="module")
def runtime_result(compile_result, update_binaries):
    bin_dir, result, programming_language, runtime = compile_result
    module_dir = os.path.dirname(os.path.realpath(__file__))
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

@pytest.mark.compiler
def test_succesful_return_code(compile_result):
    _, result, _, _ = compile_result
    assert result.return_code == 0


@pytest.mark.compiler
def test_creates_manifest(compile_result):
    bin_dir, _, _, _ = compile_result
    manifest_path = os.path.join(bin_dir, 'manifest')
    assert os.path.exists(manifest_path)


@pytest.mark.compiler
def test_creates_bot_executable(compile_result):
    bin_dir, _, _, _ = compile_result
    manifest_path = os.path.join(bin_dir, 'manifest')

    assert os.path.exists(
        os.path.join(
            bin_dir, 
            get_manifest_executable(manifest_path),
        )
    )


@pytest.mark.compiler
def test_executable_permissions(compile_result):
    bin_dir, _, _, _ = compile_result
    manifest_path = os.path.join(bin_dir, 'manifest')
    file_mode = os.stat(
        os.path.join(
            bin_dir, 
            get_manifest_executable(manifest_path),
        )
    ).st_mode

    assert file_mode == 0o100755

@pytest.mark.compiler
@pytest.mark.integration
def test_succesful_return_code(runtime_result):
    assert runtime_result.return_code == 0

@pytest.mark.compiler
@pytest.mark.integration
def test_bot_returns_correct_output(runtime_result):
    assert runtime_result.stdout.strip() in ['rock', 'paper', 'scissors']