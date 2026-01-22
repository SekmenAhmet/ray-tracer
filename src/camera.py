"""
Camera definition.
"""


class Camera:
    """
    Simple perspective camera.

    Attributes
    ----------
    position : Vector3
        Camera position.
    width : int
        Image width in pixels.
    height : int
        Image height in pixels.
    fov : float
        Field of view in degrees.
    """

    def __init__(self, position, width, height, fov):
        """
        Initialize a camera.

        Parameters
        ----------
        position : Vector3
            Camera position.
        width : int
            Image width in pixels.
        height : int
            Image height in pixels.
        fov : float
            Field of view in degrees.
        """
        self.position = position
        self.width = width
        self.height = height
        self.fov = fov

    def __str__(self):
        """
        Return a readable representation of the camera.
        """
        return f"Camera({self.position}, {self.width}, {self.height}, fov={self.fov})"
