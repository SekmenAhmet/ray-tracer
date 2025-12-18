"""
Chargement d'une scene depuis un fichier texte.
"""

from camera import Camera
from light import Light
from sphere import Sphere
from vector import Vector3


class SceneLoader:
    """
    Parse un fichier de scene et renseigne un objet Scene.

    Le format attendu est une ligne par element, avec des tokens separes
    par des espaces simples.
    """

    def __init__(self, filename, scene) -> None:
        self.filename = filename
        self.scene = scene

    def parse(self):
        """
        Parse le fichier et ajoute les objets a la scene.

        Notes
        -----
        Les lignes attendues commencent par "Camera", "Light" ou "Sphere".
        Les lignes doivent etre non vides et bien formees, sinon une
        exception peut etre levee. Chaque objet est affiche via print.
        """
        parsers = {
            "Camera": self.parse_camera,
            "Light": self.parse_light,
            "Sphere": self.parse_sphere,
        }

        with open(self.filename, "r", encoding="utf-8") as file:
            for f in file:
                words = f.strip().split(" ")

                if not words:
                    continue

                obj = parsers[words[0]](words)
                print(obj)

    def parse_camera(self, words):
        """
        Cree et ajoute une camera a partir des tokens.

        Format attendu
        --------------
        Camera x y z width height fov
        """
        position = Vector3(*map(float, words[1:4]))
        w, h = map(int, words[4:6])
        fov = float(words[6])
        obj = Camera(position, w, h, fov)
        self.scene.set_camera(obj)
        return obj

    def parse_light(self, words):
        """
        Cree et ajoute une lumiere a partir des tokens.

        Format attendu
        --------------
        Light x y z r g b intensity
        """
        position = Vector3(*map(float, words[1:4]))
        color = Vector3(*map(int, words[4:7]))
        intensity = float(words[7])
        obj = Light(position, color, intensity)
        self.scene.add_light(obj)
        return obj

    def parse_sphere(self, words):
        """
        Cree et ajoute une sphere a partir des tokens.

        Format attendu
        --------------
        Sphere x y z radius r g b
        """
        center = Vector3(*map(float, words[1:4]))
        radius = float(words[4])
        color = Vector3(*map(int, words[5:8]))

        obj = Sphere(center, radius, color)
        self.scene.add_sphere(obj)
        return obj
