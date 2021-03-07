import os
import platform
from collections import namedtuple


ProgramInfo = namedtuple(
    "ProgramInfo",
    field_names=["commit", "branch", "python_version"]
)


def get_program_info():
    return ProgramInfo(
        commit=os.environ.get("COMMIT", "unknown"),
        branch=os.environ.get("BRANCH", "unknown"),
        python_version=platform.python_version(),
    )
