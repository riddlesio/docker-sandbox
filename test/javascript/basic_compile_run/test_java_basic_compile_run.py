import os
import inspect
import pytest
import shutil

from util.subprocess import SubprocessRunner
from util.temp_dir import temp_dir
from util.test_utils import create_docker_compile_command
from util.test_utils import create_docker_runtime_command

@pytest.mark.java
@pytest.mark.compiler
@pytest.mark.runtime
def test_basic_compile_run():
    pass
