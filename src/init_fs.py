"""
Initialisation des dossiers attendus par le projet.
"""

import os

REQUIRED_DIRS = ["output", "scene"]


def init_filesystem():
    """
    Cree les dossiers requis si besoin.
    """
    for d in REQUIRED_DIRS:
        os.makedirs(d, exist_ok=True)
