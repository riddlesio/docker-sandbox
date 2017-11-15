from test.subprocess import SubprocessRunner

if __name__ == '__main__':
    args = sys.argv[1::]
    command = 'pytest' if not len(args) else 'pytest -m "{}"'.format(' '.join(args))
    result = SubprocessRunner().run(command)
    exit(result.return_code)
