"""
    Module Renderer
"""

import math
from vector import Vector3
from ray import Ray

class Renderer:
    """
    Class Renderer
    
    Attributes
    ----------
    scene : Scene
        scene to render
    camera : Camera
        camera to render
    
    """
    def __init__(self, scene, camera):
        self.scene = scene
        self.camera = camera

    def render(self):
        """
        Render the scene
        """        
        
        image = []
        for y in range(self.camera.height):
            row = []
            for x in range(self.camera.width):
                direction = self.get_ray_direction(x, y)
                ray = Ray(self.camera.position, direction)
                for sphere in self.scene.spheres:
                    t = sphere.intersect(ray)
                    if t is not None:
                        color = sphere.color
                        break
                row.append(self.scene.background_color)
            image.append(row)
        return image

    def get_ray_direction(self, x, y):
        """
        :param self: Renderer
        :param x: int
        :param y: int
        """
        px = (2 * x / self.camera.width) - 1
        py = 1 - (2 * y / self.camera.height)
        pz = -1 / math.tan(math.radians(self.camera.fov / 2))
        direction = Vector3(px, py, pz).normalize()
        return direction
