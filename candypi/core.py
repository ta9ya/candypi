# -*- coding: utf-8 -*-

import git


dir_path = '/Users/iwasa/work/mogbee'

git_repo = git.Repo(dir_path)
git_repo.git.pull()
