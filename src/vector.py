"""
Vecteur 3D minimal avec operations de base.
"""

class Vector3:
    """
    Vecteur 3D.

    Attributes
    ----------
    x : float
        Coordonnee x.
    y : float
        Coordonnee y.
    z : float
        Coordonnee z.
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        """
        Retourne une representation lisible du vecteur.
        """
        return f"({self.x}, {self.y}, {self.z})"

    def add(self, other):
        """
        Additionne deux vecteurs.

        Parameters
        ----------
        other : Vector3
            Vecteur additionne.

        Returns
        -------
        Vector3
            Somme des deux vecteurs.
        """
        return Vector3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def length(self):
        """
        Retourne la norme euclidienne.

        Returns
        -------
        float
            Longueur du vecteur.
        """
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def subtract(self, other):
        """
        Soustrait un vecteur a un autre.

        Parameters
        ----------
        other : Vector3
            Vecteur a soustraire.

        Returns
        -------
        Vector3
            Difference des deux vecteurs.
        """
        return Vector3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def multiply(self, scalar):
        """
        Multiplie le vecteur par un scalaire.

        Parameters
        ----------
        scalar : float
            Scalaire multiplicatif.

        Returns
        -------
        Vector3
            Vecteur multiplie par le scalaire.
        """
        return Vector3(
            self.x * scalar,
            self.y * scalar,
            self.z * scalar
        )

    def normalize(self):
        """
        Retourne un vecteur unitaire.

        Returns
        -------
        Vector3
            Vecteur normalise (longueur 1).

        Notes
        -----
        La longueur doit etre non nulle.
        """
        return self.multiply(1 / self.length())

    def dot(self, other):
        """
        Calcule le produit scalaire.

        Parameters
        ----------
        other : Vector3
            Autre vecteur.

        Returns
        -------
        float
            Produit scalaire des deux vecteurs.
        """
        return self.x * other.x + self.y * other.y + self.z * other.z

    def scale(self, scalar):
        """
        Alias de multiply.

        Parameters
        ----------
        scalar : float
            Scalaire multiplicatif.

        Returns
        -------
        Vector3
            Vecteur multiplie par le scalaire.
        """
        return self.multiply(scalar)
