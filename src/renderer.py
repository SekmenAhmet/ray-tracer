"""
Rendu d'une scene 3D simple avec spheres, plans et anti-aliasing.
"""

import math

from ray import Ray
from vector import Vector3


class Renderer:
    def __init__(self, scene):
        self.scene = scene

    def render(self):
        image = []

        # Anti-aliasing 2x2
        samples = [
            (0.25, 0.25),
            (0.75, 0.25),
            (0.25, 0.75),
            (0.75, 0.75),
        ]
        inv_samples = 1 / len(samples)

        for y in range(self.scene.camera.height):
            row = []
            for x in range(self.scene.camera.width):
                pixel_color = Vector3(0, 0, 0)

                for dx, dy in samples:
                    direction = self.get_ray_direction(x + dx, y + dy)
                    ray = Ray(self.scene.camera.position, direction)
                    color = self.trace_ray(ray)
                    pixel_color = pixel_color.add(color)

                pixel_color = pixel_color.scale(inv_samples)
                row.append(pixel_color)

            image.append(row)

        return image

    def trace_ray(self, ray):
        closest_t = float("inf")
        hit_obj = None

        # Spheres
        for sphere in self.scene.spheres:
            t = sphere.intersect(ray)
            if t and t < closest_t:
                closest_t = t
                hit_obj = sphere

        # Planes
        for plane in self.scene.planes:
            t = plane.intersect(ray)
            if t and t < closest_t:
                closest_t = t
                hit_obj = plane

        if hit_obj:
            return self.compute_lighting(ray, closest_t, hit_obj)

        return self.scene.background_color

    def get_ray_direction(self, x, y):
        w = self.scene.camera.width
        h = self.scene.camera.height

        aspect = w / h
        px = (2 * (x / w) - 1) * aspect
        py = 1 - 2 * (y / h)
        pz = -1 / math.tan(math.radians(self.scene.camera.fov / 2))

        return Vector3(px, py, pz).normalize()

    def compute_lighting(self, ray, t, obj):
        hit_point = ray.origin.add(ray.direction.scale(t))

        # Normale
        if hasattr(obj, "center"):  # Sphere
            normal = hit_point.subtract(obj.center).normalize()
        else:  # Plane
            normal = obj.normal

        base_color = obj.color
        final_color = base_color.scale(0.1)  # ambient

        for light in self.scene.lights:
            light_dir = light.position.subtract(hit_point).normalize()

            # Shadow ray
            shadow_origin = hit_point.add(normal.scale(0.001))
            shadow_ray = Ray(shadow_origin, light_dir)
            in_shadow = False

            for other in self.scene.spheres + self.scene.planes:
                if other != obj:
                    shadow_t = other.intersect(shadow_ray)
                    if shadow_t and shadow_t > 0:
                        in_shadow = True
                        break

            if not in_shadow:
                # Diffuse
                diffuse = max(0, normal.dot(light_dir))
                diffuse_color = base_color.scale(diffuse * light.intensity)

                # Specular (Phong)
                reflect_dir = light_dir.subtract(
                    normal.scale(2 * light_dir.dot(normal))
                )
                view_dir = ray.direction.scale(-1).normalize()
                specular = max(0, reflect_dir.dot(view_dir)) ** 32
                specular_color = light.color.scale(specular * light.intensity * 0.5)

                final_color = final_color.add(diffuse_color).add(specular_color)

        # Clamp
        final_color.x = min(255, max(0, final_color.x))
        final_color.y = min(255, max(0, final_color.y))
        final_color.z = min(255, max(0, final_color.z))

        return final_color
