import pytest

def pytest_addoption(parser):
    parser.addoption(
        '--update-binaries',
        action='store_true',
        default=False,
        help='Updates binaries in `test/bot_binaries` for use with the runtime tests'
    )

@pytest.fixture(scope='session')
def update_binaries(request):
    return request.config.getoption("--update-binaries")
