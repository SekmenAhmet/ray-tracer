"""
Definition d'une lumiere ponctuelle.
"""

from vector import Vector3


class Light:
    """
    Lumiere ponctuelle.

    Attributes
    ----------
    position : Vector3
        Position de la source.
    color : Vector3
        Couleur RGB.
    intensity : float
        Intensite (facteur de brillance).
    """

    def __init__(self, position, color=Vector3(255, 255, 255), intensity=1.0):
        """
        Initialise une source lumineuse.

        Parameters
        ----------
        position : Vector3
            Position de la lumiere.
        color : Vector3, optional
            Couleur RGB (defaut: blanc).
        intensity : float, optional
            Intensite (defaut: 1.0).
        """
        self.position = position
        self.color = color
        self.intensity = intensity

    def __str__(self):
        """
        Retourne une representation lisible de la lumiere.
        """
        return f"Light({self.position}, {self.color}, intensity={self.intensity})"
