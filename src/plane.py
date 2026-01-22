"""
Plane definition.
"""


class Plane:
    """
    Plane defined by a point, a normal, and a color.

    Attributes
    ----------
    point : Vector3
        Reference point on the plane.
    normal : Vector3
        Plane normal.
    color : Vector3
        RGB color.
    """

    def __init__(self, point, normal, color) -> None:
        """
        Initialize a plane.

        Parameters
        ----------
        point : Vector3
            Reference point on the plane.
        normal : Vector3
            Plane normal.
        color : Vector3
            RGB color.
        """
        self.point = point
        self.normal = normal
        self.color = color

    def intersect(self, ray):
        """
        Compute a ray-plane intersection.

        Parameters
        ----------
        ray : Ray
            Ray to test.

        Returns
        -------
        float or None
            Positive distance t if hit, otherwise None.
        """
        denom = self.normal.dot(ray.direction)
        if abs(denom) < 1e-6:
            return None
        t = self.point.subtract(ray.origin).dot(self.normal) / denom
        return t if t > 0 else None

    def __str__(self):
        """
        Return a readable representation of the plane.
        """
        return f"Plane({self.point}, {self.normal}, {self.color})"
