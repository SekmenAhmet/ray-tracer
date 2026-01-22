"""
Sphere definition.
"""

class Sphere:

    """
    Sphere.

    Attributes
    ----------
    center : Vector3
        Sphere center.
    radius : float
        Sphere radius.
    color : Vector3
        Sphere RGB color.
    """

    def __init__(self, center, radius, color):
        """
        Initialize a sphere.

        Parameters
        ----------
        center : Vector3
            Sphere center.
        radius : float
            Sphere radius.
        color : Vector3
            RGB color.
        """
        self.center = center
        self.radius = radius
        self.color = color

    def __str__(self):
        """
        Return a readable representation of the sphere.
        """
        return f"Sphere({self.center}, {self.radius}, {self.color})"

    def intersect(self, ray):
        """
        Compute a ray-sphere intersection.

        Parameters
        ----------
        ray : Ray
            Ray to test.

        Returns
        -------
        float or None
            Smallest positive t if hit, otherwise None.
        """
        oc = ray.origin.subtract(self.center)
        a = ray.direction.dot(ray.direction)
        b = 2 * oc.dot(ray.direction)
        c = oc.dot(oc) - self.radius ** 2
        discriminant = b ** 2 - 4 * a * c

        if discriminant < 0:
            return None

        t1 = (-b - discriminant ** 0.5) / (2 * a)
        t2 = (-b + discriminant ** 0.5) / (2 * a)

        if t1 > 0 and t2 > 0:
            return min(t1, t2)
        if t1 > 0:
            return t1
        if t2 > 0:
            return t2
        return None
