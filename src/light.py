"""
Point light definition.
"""

from vector import Vector3


class Light:
    """
    Point light.

    Attributes
    ----------
    position : Vector3
        Light position.
    color : Vector3
        RGB color.
    intensity : float
        Intensity multiplier.
    """

    def __init__(self, position, color=Vector3(255, 255, 255), intensity=1.0):
        """
        Initialize a light source.

        Parameters
        ----------
        position : Vector3
            Light position.
        color : Vector3, optional
            RGB color (default: white).
        intensity : float, optional
            Intensity (default: 1.0).
        """
        self.position = position
        self.color = color
        self.intensity = intensity

    def __str__(self):
        """
        Return a readable representation of the light.
        """
        return f"Light({self.position}, {self.color}, intensity={self.intensity})"
