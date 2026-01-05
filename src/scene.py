"""
Conteneur de la scene (camera, objets et lumieres).
"""

from vector import Vector3


class Scene:
    """
    Regroupe les elements de la scene.

    Attributes
    ----------
    camera : Camera or None
        Camera active.
    spheres : list[Sphere]
        Liste des spheres.
    planes : list[Plane]
        Liste des plans.
    lights : list[Light]
        Liste des lumieres.
    background_color : Vector3
        Couleur de fond.
    """

    def __init__(self):
        """
        Initialise une scene vide.
        """
        self.camera = None
        self.spheres = []
        self.lights = []
        self.planes = []
        self.background_color = Vector3(0, 0, 0)

    def set_camera(self, camera):
        """
        Definit la camera de la scene.

        Parameters
        ----------
        camera : Camera
            Camera a utiliser.
        """
        self.camera = camera

    def add_sphere(self, sphere):
        """
        Ajoute une sphere a la scene.

        Parameters
        ----------
        sphere : Sphere
            Sphere a ajouter.
        """
        self.spheres.append(sphere)

    def add_light(self, light):
        """
        Ajoute une lumiere a la scene.

        Parameters
        ----------
        light : Light
            Lumiere a ajouter.
        """
        self.lights.append(light)

    def add_plane(self, plane):
        """
        Ajoute un plan a la scene.

        Parameters
        ----------
        plane : Plane
            Plan a ajouter.
        """
        self.planes.append(plane)
