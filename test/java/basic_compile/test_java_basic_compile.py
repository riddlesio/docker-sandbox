import os
import inspect
import pytest
import shutil

from util.subprocess import SubprocessRunner
from util.temp_dir import temp_dir
from util.test_utils import create_docker_compile_command

@pytest.mark.java
@pytest.mark.compiler
def test_basic_compile():
    module_dir = os.path.dirname(os.path.realpath(__file__))

    with temp_dir() as path:

        # Step 1: Create the required folder structure
        source_dir = os.path.join(path, 'source')
        bin_dir = os.path.join(path, 'bin')
        
        os.mkdir(source_dir)
        os.mkdir(bin_dir)

        shutil.copyfile(os.path.join(module_dir, 'java_basic_compile_bot.java'), source_dir)

        # Step 2: Run the compiler and get the output
        command = create_docker_compile_command(source_dir, bin_dir, '')
        result = SubprocessRunner().run(command)

        assert result.return_code == 0
        assert os.path.exists(os.path.join(bin_dir, 'run_ai.jar'))
