import os
import pytest
from util.subprocess import SubprocessRunner
from util.temp_dir import temp_dir
from util.test_utils import create_docker_runtime_command

@pytest.mark.java
@pytest.mark.runtime
def test_basic_run():
    module_dir = os.path.dirname(os.path.realpath(__file__))

    with temp_dir() as path:

        # Step 1: Create the required folder structure
        shutil.copyfile(os.path.join(module_dir, 'basic_run_bot.js'), path)

        # Step 2: Run the compiler and get the output
        command = create_docker_runtime_command(source_dir, bin_dir, '')
        result = SubprocessRunner().run(command)

        assert result.return_code == 0
        assert result.stdout.strip() in ['rock', 'paper', 'scissors']
