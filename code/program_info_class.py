import os
import platform


class ProgramInfoClass:
    def __init__(self, commit, branch, python_version):
        self.commit = commit
        self.branch = branch
        self.python_version = python_version


def get_program_info_class():
    return ProgramInfoClass(
        commit=os.environ.get("COMMIT", "unknown"),
        branch=os.environ.get("BRANCH", "unknown"),
        python_version=platform.python_version(),
    )
