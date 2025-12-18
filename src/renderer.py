"""
Rendu d'une scene 3D simple avec spheres et lumiere ponctuelle.

Le rendu produit une image sous forme de grille de couleurs (Vector3).
"""

import math

from ray import Ray
from vector import Vector3


class Renderer:
    """
    Effectue le rendu d'une scene.

    Attributes
    ----------
    scene : Scene
        Scene a rendre.
    """

    def __init__(self, scene):
        self.scene = scene

    def render(self):
        """
        Rend la scene pixel par pixel.

        Returns
        -------
        list[list[Vector3]]
            Image sous forme de grille de couleurs RGB.
        """

        image = []
        for y in range(self.scene.camera.height):
            row = []
            for x in range(self.scene.camera.width):
                direction = self.get_ray_direction(x, y)
                ray = Ray(self.scene.camera.position, direction)
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
        Calcule la direction du rayon pour un pixel.

        Parameters
        ----------
        x : int
            Coordonne x du pixel.
        y : int
            Coordonne y du pixel.

        Returns
        -------
        Vector3
            Direction normalisee dans l'espace camera.
        """
        px = (2 * x / self.scene.camera.width) - 1
        py = 1 - (2 * y / self.scene.camera.height)
        pz = -1 / math.tan(math.radians(self.scene.camera.fov / 2))
        direction = Vector3(px, py, pz).normalize()
        return direction

    def compute_lighting(self, ray, t, sphere):
        """
        Calcule l'eclairage au point d'intersection via le modele de Phong.

        Parameters
        ----------
        ray : Ray
            Rayon primaire ayant touche la sphere.
        t : float
            Distance d'intersection.
        sphere : Sphere
            Sphere intersectee.

        Returns
        -------
        Vector3
            Couleur finale avec ombres, composantes ambiante/diffuse/speculaire,
            et valeurs clampes dans [0, 255].
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
            shadow_ray_origin = hit_point.add(
                normal.scale(0.001)
            )  # léger décalage pour éviter l'auto-intersection
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
                reflect_dir = light_dir.subtract(
                    normal.scale(2 * light_dir.dot(normal))
                )
                view_dir = ray.direction.scale(-1).normalize()
                specular_intensity = (
                    max(0, reflect_dir.dot(view_dir)) ** 32
                )  # shininess = 32

                # Contribution de cette lumière
                diffuse_color = sphere.color.scale(diffuse_intensity * light.intensity)
                specular_color = light.color.scale(
                    specular_intensity * light.intensity * 0.5
                )

                final_color = final_color.add(diffuse_color).add(specular_color)

        # Clamper les valeurs entre 0 et 255
        final_color.x = min(255, max(0, final_color.x))
        final_color.y = min(255, max(0, final_color.y))
        final_color.z = min(255, max(0, final_color.z))

        return final_color
