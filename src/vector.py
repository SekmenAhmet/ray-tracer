"""
Minimal 3D vector with basic operations.
"""

class Vector3:
    """
    3D vector.

    Attributes
    ----------
    x : float
        X coordinate.
    y : float
        Y coordinate.
    z : float
        Z coordinate.
    """
    def __init__(self, x, y, z):
        """
        Initialize a 3D vector.

        Parameters
        ----------
        x : float
            X coordinate.
        y : float
            Y coordinate.
        z : float
            Z coordinate.
        """
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        """
        Return a readable representation of the vector.
        """
        return f"({self.x}, {self.y}, {self.z})"

    def add(self, other):
        """
        Add two vectors.

        Parameters
        ----------
        other : Vector3
            Vector to add.

        Returns
        -------
        Vector3
            Sum of the two vectors.
        """
        return Vector3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def length(self):
        """
        Return the Euclidean length.

        Returns
        -------
        float
            Vector length.
        """
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def subtract(self, other):
        """
        Subtract another vector.

        Parameters
        ----------
        other : Vector3
            Vector to subtract.

        Returns
        -------
        Vector3
            Difference between the two vectors.
        """
        return Vector3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def multiply(self, scalar):
        """
        Multiply the vector by a scalar.

        Parameters
        ----------
        scalar : float
            Multiplicative scalar.

        Returns
        -------
        Vector3
            Vector scaled by the scalar.
        """
        return Vector3(
            self.x * scalar,
            self.y * scalar,
            self.z * scalar
        )

    def normalize(self):
        """
        Return a unit vector.

        Returns
        -------
        Vector3
            Normalized vector (length 1).

        Notes
        -----
        The length must be non-zero.
        """
        return self.multiply(1 / self.length())

    def dot(self, other):
        """
        Compute the dot product.

        Parameters
        ----------
        other : Vector3
            Other vector.

        Returns
        -------
        float
            Dot product of the two vectors.
        """
        return self.x * other.x + self.y * other.y + self.z * other.z

    def scale(self, scalar):
        """
        Alias for multiply.

        Parameters
        ----------
        scalar : float
            Multiplicative scalar.

        Returns
        -------
        Vector3
            Vector scaled by the scalar.
        """
        return self.multiply(scalar)
