import os

cache_path = '/tmp/myScriptCache'
tmp_repo_path = 'foo-bar'


def checkExists(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


def getUniHashKey(path: str) -> str:
    return str(hash(path))


def cloneRepoFromGithub(path: str, repo: str):
    checkExists(cache_path)
    os.chdir(cache_path)
    checkExists(os.path.join(cache_path, path))
    os.chdir(os.path.join(cache_path, path))
    os.system(f'git clone {repo} {tmp_repo_path}')


def args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-p',
                        '--remotePath',
                        help='Path to the folder on remote server',
                        required=True)
    parser.add_argument('-r', '--repo', help='Repository URL', required=True)
    parser.add_argument('-s', '--ssh', help='ssh user', required=True)
    parser.add_argument('-P', '--port', help='ssh port', required=True)
    return parser.parse_args()


if __name__ == '__main__':
    runtime_arg = args()
    tmp_dir = getUniHashKey(runtime_arg.remotePath)
    cloneRepoFromGithub(tmp_dir, runtime_arg.repo)

    # use rsync to sync the repo to remote with ssh
    print(
        f'rsync -rv -e "ssh -p {runtime_arg.port}" {os.path.join(cache_path, tmp_dir, tmp_repo_path)} {runtime_arg.ssh}:{runtime_arg.remotePath}'
    )
    input('== continue? ==')
    os.system(
        f'rsync -rv -e "ssh -p {runtime_arg.port}" {os.path.join(cache_path, tmp_dir, tmp_repo_path)} {runtime_arg.ssh}:{runtime_arg.remotePath}'
    )
