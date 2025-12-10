"""
    Module Main
"""

from scene import Scene
from sphere import Sphere
from vector import Vector3
from camera import Camera
from renderer import Renderer
from image_writer import save_ppm
from light import Light

scene = Scene()

sphere1 = Sphere(
    center=Vector3(0, 0, -5),
    radius=1,
    color=Vector3(255, 0, 0)
)
scene.add_sphere(sphere1)

sphere2 = Sphere(
    center=Vector3(2, 0, -6),
    radius=0.8,
    color=Vector3(0, 0, 255)
)
scene.add_sphere(sphere2)

sphere3 = Sphere(
    center=Vector3(-2, 0, -6),
    radius=0.8,
    color=Vector3(0, 255, 0)
)
scene.add_sphere(sphere3)

light1 = Light(
    position=Vector3(5, 5, 0),
    color=Vector3(255, 255, 255),
    intensity=1.0
)
scene.add_light(light1)

camera = Camera(
    position=Vector3(0, 0, 0),
    width=800,
    height=600,
    fov=90
)

renderer = Renderer(scene, camera)
image = renderer.render()
save_ppm('output/image.ppm', image, camera.width, camera.height)
