import os
import pytest
from test.subprocess import SubprocessRunner


@pytest.mark.java
@pytest.mark.runtime
def test_basic_run():
    module_dir = os.path.dirname(inspect.getfile(inspect))

    with temp_dir() as path:

        # Step 1: Create the required folder structure
        shutil.copyfile(os.path.join(module_dir, 'java_basic_compile_bot.jar'), path)

        # Step 2: Run the compiler and get the output
        command = create_docker_command(source_dir, bin_dir, '')
        result = SubprocessRunner().run(command)

        assert result.return_code == 0
        assert result.stdout.strip() in ['rock', 'paper', 'scissors']
