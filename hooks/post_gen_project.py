#!/usr/bin/env python
import os
import textwrap

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def install_hooks():
    """
    Install git hooks to make life easier.
    """

    git_hooks_path = os.path.join(PROJECT_DIRECTORY, '.git/hooks/')

    if not os.path.exists(git_hooks_path):
        os.makedirs(git_hooks_path)

    pre_push_path = os.path.join(git_hooks_path, 'pre-push')

    with open(pre_push_path, 'w') as dest:
        with open(os.path.join(PROJECT_DIRECTORY, 'pre-push')) as src:
            dest.write(src.read())

    os.chmod(pre_push_path, 0o755)

    remove_file('pre-push')


if __name__ == '__main__':

    open_source = '{{ cookiecutter.open_source }}'.lower()
    if not open_source == 'y' or open_source == 'yes':
        remove_file('LICENSE')

    install_hooks()
