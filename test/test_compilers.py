import os
import pytest
import shutil
from contextlib import contextmanager

from util.subprocess import SubprocessRunner
from util.temp_dir import temp_dir
from util.test_utils import create_docker_compile_command
from util.test_utils import compiler_image
from util.test_utils import get_manifest_executable

FIXTURES = [
    ('javascript', 'basic_bot.js'),
    ('php', 'basic_bot.php'),
]

def as_id(datum):
    return '{} - {}'.format(datum[0], datum[1])

def as_param(datum):
    mark = getattr(pytest.mark, datum[0])
    return pytest.param(datum, marks=mark)

@pytest.fixture(
    autouse=True,
    ids=as_id,
    params=list(map(as_param, FIXTURES)),
    scope="module",
)
def setup(request):
    programming_language, bot_file = request.param
    module_dir = os.path.dirname(os.path.realpath(__file__))

    # Note: all temp dirs should be created within `/tmp` instead of `/var`
    # as macOS cannot volume mount folders located in `/var` by default.
    # See https://docs.docker.com/docker-for-mac/osxfs/#namespaces for more
    # info.
    with temp_dir(dir='/tmp') as path:

        # Step 1: Create the required folder structure
        source_dir = os.path.join(path, 'source')
        bin_dir = os.path.join(path, 'bin')

        os.mkdir(source_dir)
        os.mkdir(bin_dir)

        shutil.copyfile(
            os.path.join(module_dir, 'bot_sources/{}/{}'.format(programming_language, bot_file)),
            os.path.join(source_dir, bot_file)
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


@pytest.mark.compiler
def test_succesful_return_code(setup):
    _, result = setup
    assert result.return_code == 0


@pytest.mark.compiler
def test_creates_manifest(setup):
    bin_dir, _ = setup
    manifest_path = os.path.join(bin_dir, 'manifest')
    assert os.path.exists(manifest_path)


@pytest.mark.compiler
def test_creates_bot_executable(setup):
    bin_dir, _ = setup
    manifest_path = os.path.join(bin_dir, 'manifest')

    assert os.path.exists(
        get_manifest_executable(
            manifest_path,
            bin_dir,
        )
    )


@pytest.mark.compiler
def test_executable_permissions(setup):
    bin_dir, _ = setup
    manifest_path = os.path.join(bin_dir, 'manifest')
    file_mode = os.stat(
        get_manifest_executable(
            manifest_path,
            bin_dir,
        )
    ).st_mode

    assert file_mode == 0o100755
