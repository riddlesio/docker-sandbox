import shutil
import tempfile

from contextlib import contextmanager


@contextmanager
def temp_dir(dir=None):
    abs_path = tempfile.mkdtemp(dir=dir)
    yield abs_path
    shutil.rmtree(abs_path)
