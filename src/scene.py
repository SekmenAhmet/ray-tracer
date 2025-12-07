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
    
    """
    def __init__(self):
        self.spheres = []
        self.background_color = Vector3(0, 0, 0)

    def add_sphere(self, sphere):
        """
        :param self: Scene
        :param sphere: Sphere
        """
        self.spheres.append(sphere)
