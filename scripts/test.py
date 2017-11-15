from test.subprocess import SubprocessRunner

if __name__ == '__main__':
    args = sys.argv[1::]
    SubprocessRunner().run('pytest {}'.format(' '.join(args)))
