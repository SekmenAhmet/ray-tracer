"""
    Module Sphere
"""

class Sphere:

    """
    Class Sphere
    
    Attributes
    ----------
    center : Vector3
        center of the sphere
    radius : float
        radius of the sphere
    color : Color
        color of the sphere
    
    """

    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color

    def __str__(self):
        return f"Sphere({self.center}, {self.radius}, {self.color})"

    def intersect(self, ray):
        """
        :param self: Sphere
        :param ray: Ray
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
