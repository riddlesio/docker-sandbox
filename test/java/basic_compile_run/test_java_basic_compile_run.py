import os
import inspect
import pytest
import shutil

from test.subprocess import SubprocessRunner
from test.test_utils import create_docker_command

@pytest.mark.java
@pytest.mark.compiler
@pytest.mark.runtime
def test_basic_compile_run():
    module_dir = os.path.dirname(inspect.getfile(inspect))

    with temp_dir() as path:

        # Step 1: Create the required folder structure
        source_dir = os.path.join(path, 'source')
        bin_dir = os.path.join(path, 'bin')
        
        os.mkdir(source_dir)
        os.mkdir(bin_dir)

        shutil.copyfile(os.path.join(module_dir, 'java_basic_compile_bot.java'), source_dir)

        # Step 2: Run the compiler and get the output
        command = create_docker_command(source_dir, bin_dir, '')
        result = SubprocessRunner().run(command)

        assert result.return_code == 0
        assert os.path.exists(os.path.join(bin_dir, 'run_ai.jar'))

        # Step 2: Run the compiler and get the output
        command = 'cat $(java_basic_compile_scenario.txt) | xargs | ' + create_docker_command(bin_dir, '')
        result = SubprocessRunner().run(command)

        assert result.return_code == 0
        assert result.stdout.strip() in ['rock', 'paper', 'scissors']
