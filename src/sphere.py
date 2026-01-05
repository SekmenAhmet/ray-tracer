"""
Definition d'une sphere.
"""

class Sphere:

    """
    Sphere.

    Attributes
    ----------
    center : Vector3
        Centre de la sphere.
    radius : float
        Rayon de la sphere.
    color : Vector3
        Couleur RGB de la sphere.
    """

    def __init__(self, center, radius, color):
        """
        Initialise une sphere.

        Parameters
        ----------
        center : Vector3
            Centre de la sphere.
        radius : float
            Rayon de la sphere.
        color : Vector3
            Couleur RGB.
        """
        self.center = center
        self.radius = radius
        self.color = color

    def __str__(self):
        """
        Retourne une representation lisible de la sphere.
        """
        return f"Sphere({self.center}, {self.radius}, {self.color})"

    def intersect(self, ray):
        """
        Calcule l'intersection rayon-sphere.

        Parameters
        ----------
        ray : Ray
            Rayon a tester.

        Returns
        -------
        float or None
            Plus petite distance t positive si intersection, sinon None.
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
