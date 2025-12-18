import os

REQUIRED_DIRS = ["output", "scene"]


def init_filesystem():
    for d in REQUIRED_DIRS:
        os.makedirs(d, exist_ok=True)
