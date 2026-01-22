"""
Ray definition.
"""

class Ray:
    """
    3D ray.

    Attributes
    ----------
    origin : Vector3
        Ray origin.
    direction : Vector3
        Ray direction.
    """
    def __init__(self, origin, direction):
        """
        Initialize a ray.

        Parameters
        ----------
        origin : Vector3
            Ray origin.
        direction : Vector3
            Ray direction.
        """
        self.origin = origin
        self.direction = direction

    def __str__(self):
        """
        Return a readable representation of the ray.
        """
        return f"Ray({self.origin}, {self.direction})"

    def point_at(self, t):
        """
        Compute a point along the ray.

        Parameters
        ----------
        t : float
            Scalar distance along the ray.

        Returns
        -------
        Vector3
            Point at distance t.
        """
        return self.origin.add(self.direction.multiply(t))
