"""
Initialize the directories expected by the project.
"""

import os

REQUIRED_DIRS = ["output", "scene"]


def init_filesystem():
    """
    Create required directories if needed.
    """
    for d in REQUIRED_DIRS:
        os.makedirs(d, exist_ok=True)
