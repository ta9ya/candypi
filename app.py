# -*- coding: utf-8 -*-

from flask import Flask, request
import argparse
import git
import os


parser = argparse.ArgumentParser()
parser.add_argument('arg1', help='fullpath of git root directory ')
args = parser.parse_args()


app = Flask(__name__)


def create_git_repo(dir_path):
    """create git instance
    
    Args:
        dir_path (string): fullpath of git root directory
    
    Raises:
        FileExistsError: dir_path does not exist
        FileExistsError: dir_path does not have .git directory
    
    Returns:
        [type]: [description]
    """

    # exsist check
    if os.path.exists(dir_path):
        pass
    else:
        raise FileExistsError('the directory does not exist.')

    # .git directory check
    if os.path.exists(dir_path + '/.git'):
        pass
    else:
        raise FileExistsError('the directory does not have .git directory')

    return git.Repo(dir_path)


@app.route('/', methods=['POST'])
def gitpull():
    data = request.get_data()
    git_repo.git.pull()
    print(args.arg1)
    print(data)
    return data


if __name__ == '__main__':
    global git_repo
    git_repo = create_git_repo(args.args1)
    app.run(port=50000, debug=True)
