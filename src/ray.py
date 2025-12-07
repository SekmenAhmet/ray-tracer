"""
    Module Ray
"""

class Ray:
    """
    Class Ray
    
    Attributes
    ----------
    origin : Vector3
        origin of the ray
    direction : Vector3
        direction of the ray
    
    """
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def __str__(self):
        return f"Ray({self.origin}, {self.direction})"

    def point_at(self, t):
        """
        :param self: Ray
        :param t: float
        """
        return self.origin.add(self.direction.multiply(t))
