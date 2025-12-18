"""
Definition de la camera.
"""


class Camera:
    """
    Camera perspective simple.

    Attributes
    ----------
    position : Vector3
        Position de la camera.
    width : int
        Largeur de l'image en pixels.
    height : int
        Hauteur de l'image en pixels.
    fov : float
        Champ de vision en degres.
    """

    def __init__(self, position, width, height, fov):
        self.position = position
        self.width = width
        self.height = height
        self.fov = fov

    def __str__(self):
        """
        Retourne une representation lisible de la camera.
        """
        return f"Camera({self.position}, {self.width}, {self.height}, fov={self.fov})"
