"""
    Module Scene
"""

from vector import Vector3

class Scene:
    """
    Class Scene

    Attributes
    ----------
    spheres : list
        list of spheres
    lights : list
        list of lights

    """
    def __init__(self):
        self.spheres = []
        self.lights = []
        self.background_color = Vector3(0, 0, 0)

    def add_sphere(self, sphere):
        """
        :param self: Scene
        :param sphere: Sphere
        """
        self.spheres.append(sphere)

    def add_light(self, light):
        """
        :param self: Scene
        :param light: Light
        """
        self.lights.append(light)
