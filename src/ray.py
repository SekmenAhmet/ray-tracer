"""
Definition d'un rayon.
"""

class Ray:
    """
    Rayon 3D.

    Attributes
    ----------
    origin : Vector3
        Origine du rayon.
    direction : Vector3
        Direction du rayon.
    """
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def __str__(self):
        """
        Retourne une representation lisible du rayon.
        """
        return f"Ray({self.origin}, {self.direction})"

    def point_at(self, t):
        """
        Calcule un point le long du rayon.

        Parameters
        ----------
        t : float
            Distance scalaire le long du rayon.

        Returns
        -------
        Vector3
            Point a la distance t.
        """
        return self.origin.add(self.direction.multiply(t))
