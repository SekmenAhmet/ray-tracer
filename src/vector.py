"""
    Module Vector3
"""

class Vector3:
    """
    Class Vector3
    
    Attributes
    ----------
    x : float
        x coordinate
    y : float
        y coordinate
    z : float
        z coordinate
    
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def add(self, other):
        """        
        :param self: Vector3
        :param other: Vector3
        """
        return Vector3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def length(self):
        """
        :param: self
        """
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def subtract(self, other):
        """
        :param self: Vector3
        :param other: Vector3
        """
        return Vector3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def multiply(self, scalar):
        """
        :param self: Vector3
        :param other: scalar
        """
        return Vector3(
            self.x * scalar,
            self.y * scalar,
            self.z * scalar
        )

    def normalize(self):
        """
        :param self: Vector3
        """
        return self.multiply(1 / self.length())

    def dot(self, other):
        """
        :param self: Vector3
        :param other: Vector3
        """
        return self.x * other.x + self.y * other.y + self.z * other.z

    def scale(self, scalar):
        """
        Alias for multiply method
        :param self: Vector3
        :param scalar: float
        """
        return self.multiply(scalar)
