"""
Definition d'un plan.
"""


class Plane:
    """
    Plan defini par un point, une normale et une couleur.

    Attributes
    ----------
    point : Vector3
        Point de reference sur le plan.
    normal : Vector3
        Normale du plan.
    color : Vector3
        Couleur RGB.
    """

    def __init__(self, point, normal, color) -> None:
        """
        Initialise un plan.

        Parameters
        ----------
        point : Vector3
            Point de reference sur le plan.
        normal : Vector3
            Normale du plan.
        color : Vector3
            Couleur RGB.
        """
        self.point = point
        self.normal = normal
        self.color = color

    def intersect(self, ray):
        """
        Calcule l'intersection rayon-plan.

        Parameters
        ----------
        ray : Ray
            Rayon a tester.

        Returns
        -------
        float or None
            Distance t positive si intersection, sinon None.
        """
        denom = self.normal.dot(ray.direction)
        if abs(denom) < 1e-6:
            return None
        t = self.point.subtract(ray.origin).dot(self.normal) / denom
        return t if t > 0 else None

    def __str__(self):
        """
        Retourne une representation lisible du sol.
        """
        return f"Plane({self.point}, {self.normal}, {self.color})"
