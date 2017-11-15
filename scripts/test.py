import os
import sys
from util.subprocess import SubprocessRunner

if __name__ == '__main__':
    args = sys.argv[1::]
    command = 'pytest' if not len(args) else 'pytest -m "{}"'.format(' '.join(args))
    print(command)
    result = SubprocessRunner().run(command)
    print(result.stdout)
    print(result.stderr)
    exit(result.return_code)
