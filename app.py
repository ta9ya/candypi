# -*- coding: utf-8 -*-


import argparse
import datetime
from pathlib import Path

import git
from flask import Flask, request

parser = argparse.ArgumentParser()
parser.add_argument('arg1', help='the full path of the git directory')
parser.add_argument('-b', '--branch', default='master', help='target branch (Default is the master)')
args = parser.parse_args()


app = Flask(__name__)


def print_candypi(text):
    dt_now = datetime.datetime.now()
    print('[CanDyPi] {time} {statement}'.format(time=dt_now.strftime('%Y-%m-%d %H:%M:%S'), statement=text))


def check_directory(dir_path):
    """create git instance
    
    Args:
        dir_path (string): fullpath of git root directory
    
    Raises:
        FileExistsError: dir_path does not exist
        FileExistsError: dir_path does not have .git directory
    
    Returns:
        string: directory path
    """

    p = Path(dir_path)

    # exsist check
    if p.exists():
        pass
    else:
        raise FileExistsError('the directory does not exist.')

    # .git directory check
    git_p = p / '.git'
    if git_p.exists():
        pass
    else:
        raise FileExistsError('the directory does not have .git directory')

    return dir_path


@app.route('/', methods=['POST'])
def gitpull():
    data = request.get_json()
    ref = data.get('ref')
    print_candypi(ref)
    
    target_branch = args.branch

    if ref.find(target_branch) > 0:
        git_repo.git.checkout(target_branch)
        git_repo.git.pull()
        print_candypi('RUN pull command')
        return 'complete pull action'
    else:
        return 'not target branch'


if __name__ == '__main__':
    global git_repo
    git_repo = git.Repo(check_directory(args.arg1))

    target_branch = args.branch
    print_candypi('target branch is {}'.format(target_branch))

    app.run(port=50000, debug=True)
