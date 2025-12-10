"""
    Module Light
"""

from vector import Vector3

class Light:
    """
    Class Light

    Attributes
    ----------
    position : Vector3
        position of the light source
    color : Vector3
        color of the light (RGB values)
    intensity : float
        intensity of the light (brightness factor)

    """

    def __init__(self, position, color=Vector3(255, 255, 255), intensity=1.0):
        """
        Initialize a light source

        :param position: Vector3 - position of the light in 3D space
        :param color: Vector3 - RGB color of the light (default: white)
        :param intensity: float - brightness intensity (default: 1.0)
        """
        self.position = position
        self.color = color
        self.intensity = intensity

    def __str__(self):
        return f"Light({self.position}, {self.color}, intensity={self.intensity})"

