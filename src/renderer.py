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
                color = self.scene.background_color
                for sphere in self.scene.spheres:
                    t = sphere.intersect(ray)
                    if t is not None:
                        color = self.compute_lighting(ray, t, sphere)
                        break
                row.append(color)
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

    def compute_lighting(self, ray, t, sphere):
        """
        Compute lighting for intersection point using Phong illumination model

        :param ray: Ray - the ray that hit the sphere
        :param t: float - intersection distance
        :param sphere: Sphere - the sphere that was hit
        :return: Vector3 - final color with lighting
        """
        # Point d'intersection
        hit_point = ray.origin.add(ray.direction.scale(t))

        # Normale au point d'intersection
        normal = hit_point.subtract(sphere.center).normalize()

        # Couleur ambiante (un peu de lumière même dans l'ombre)
        ambient = 0.1
        final_color = sphere.color.scale(ambient)

        # Pour chaque lumière de la scène
        for light in self.scene.lights:
            # Direction vers la lumière
            light_dir = light.position.subtract(hit_point).normalize()

            # Test d'ombre : lancer un rayon vers la lumière
            shadow_ray_origin = hit_point.add(normal.scale(0.001))  # léger décalage pour éviter l'auto-intersection
            shadow_ray = Ray(shadow_ray_origin, light_dir)
            in_shadow = False

            for other_sphere in self.scene.spheres:
                if other_sphere != sphere:
                    shadow_t = other_sphere.intersect(shadow_ray)
                    if shadow_t is not None and shadow_t > 0:
                        in_shadow = True
                        break

            if not in_shadow:
                # Éclairage diffus (Lambert)
                diffuse_intensity = max(0, normal.dot(light_dir))

                # Éclairage spéculaire (Phong)
                reflect_dir = light_dir.subtract(normal.scale(2 * light_dir.dot(normal)))
                view_dir = ray.direction.scale(-1).normalize()
                specular_intensity = max(0, reflect_dir.dot(view_dir)) ** 32  # shininess = 32

                # Contribution de cette lumière
                diffuse_color = sphere.color.scale(diffuse_intensity * light.intensity)
                specular_color = light.color.scale(specular_intensity * light.intensity * 0.5)

                final_color = final_color.add(diffuse_color).add(specular_color)

        # Clamper les valeurs entre 0 et 255
        final_color.x = min(255, max(0, final_color.x))
        final_color.y = min(255, max(0, final_color.y))
        final_color.z = min(255, max(0, final_color.z))

        return final_color
