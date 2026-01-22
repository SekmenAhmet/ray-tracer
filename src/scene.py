"""
Scene container (camera, objects, and lights).
"""

from vector import Vector3


class Scene:
    """
    Group the elements of a scene.

    Attributes
    ----------
    camera : Camera or None
        Active camera.
    spheres : list[Sphere]
        List of spheres.
    planes : list[Plane]
        List of planes.
    lights : list[Light]
        List of lights.
    background_color : Vector3
        Background color.
    """

    def __init__(self):
        """
        Initialize an empty scene.
        """
        self.camera = None
        self.spheres = []
        self.lights = []
        self.planes = []
        self.background_color = Vector3(0, 0, 0)

    def set_camera(self, camera):
        """
        Set the scene camera.

        Parameters
        ----------
        camera : Camera
            Camera to use.
        """
        self.camera = camera

    def add_sphere(self, sphere):
        """
        Add a sphere to the scene.

        Parameters
        ----------
        sphere : Sphere
            Sphere to add.
        """
        self.spheres.append(sphere)

    def add_light(self, light):
        """
        Add a light to the scene.

        Parameters
        ----------
        light : Light
            Light to add.
        """
        self.lights.append(light)

    def add_plane(self, plane):
        """
        Add a plane to the scene.

        Parameters
        ----------
        plane : Plane
            Plane to add.
        """
        self.planes.append(plane)

    def clear(self):
        """
        Reset the scene (camera and objects).
        """
        self.camera = None
        self.spheres.clear()
        self.lights.clear()
        self.planes.clear()
