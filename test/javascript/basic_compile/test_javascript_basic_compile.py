import os
import pytest
import shutil

from util.subprocess import SubprocessRunner
from util.temp_dir import temp_dir
from util.test_utils import create_docker_compile_command
from util.test_utils import compiler_image
from util.test_utils import get_manifest_executable


@pytest.mark.javascript
@pytest.mark.compiler
def test_basic_compile():
    module_dir = os.path.dirname(os.path.realpath(__file__))

    with temp_dir() as path:

        # Step 1: Create the required folder structure
        source_dir = os.path.join(path, 'source')
        bin_dir = os.path.join(path, 'bin')

        os.mkdir(source_dir)
        os.mkdir(bin_dir)

        shutil.copyfile(
            os.path.join(module_dir, 'basic_compile_bot.js'),
            os.path.join(source_dir, 'basic_compile_bot.js')
        )

        # Step 2: Run the compiler and get the output
        command = create_docker_compile_command(
            source_dir, bin_dir, compiler_image('javascript'))
        result = SubprocessRunner().run(command)

        manifest_path = os.path.join(bin_dir, 'manifest')
        assert result.return_code == 0
        assert os.path.exists(manifest_path)
        assert os.path.exists(os.path.join(bin_dir, 'basic_compile_bot.js'))

        file_mode = os.stat(get_manifest_executable(
            manifest_path, bin_dir)).st_mode
        assert file_mode == 0o100755
