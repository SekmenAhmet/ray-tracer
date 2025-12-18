"""
Point d'entree du ray tracer.

Charge une scene depuis un fichier, lance le rendu et ecrit une image PPM.
Ce module est concu pour etre execute directement via `python src/main.py`.
"""

from image_writer import save_ppm
from init_fs import init_filesystem
from renderer import Renderer
from scene import Scene
from sceneLoader import SceneLoader

init_filesystem()

scene = Scene()
loader = SceneLoader("scene/scene1.txt", scene)

loader.parse()


renderer = Renderer(scene)
image = renderer.render()
save_ppm("output/image.ppm", image, scene.camera.width, scene.camera.height)
