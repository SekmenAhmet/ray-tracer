"""
Build a Scene instance from parsed descriptions at time t.
"""

from camera import Camera
from light import Light
from sphere import Sphere
from plane import Plane
from vector import Vector3


def eval_color(c, t):
    if isinstance(c[0], tuple):
        return Vector3(
            c[0][0] + (c[1][0] - c[0][0]) * t,
            c[0][1] + (c[1][1] - c[0][1]) * t,
            c[0][2] + (c[1][2] - c[0][2]) * t,
        )
    return Vector3(*c)

def eval_anim(v, t):
    """
    Evaluate an animated value at time t.

    Parameters
    ----------
    v : float or tuple[float, float]
        Static value or (start, end) range.
    t : float
        Normalized time in [0, 1].

    Returns
    -------
    float
        Interpolated value.
    """
    if isinstance(v, tuple):
        return v[0] + (v[1] - v[0]) * t
    return v

def build_scene_at_t(scene, camera_desc, objects, t):
    """
    Populate a Scene with camera and objects at time t.

    Parameters
    ----------
    scene : Scene
        Scene to populate.
    camera_desc : dict or None
        Camera description or None if absent.
    objects : list[dict]
        Object descriptions to instantiate.
    t : float
        Normalized time in [0, 1].
    """
    scene.clear()

    if camera_desc:
        cx = eval_anim(camera_desc["x"], t)
        cy = eval_anim(camera_desc["y"], t)
        cz = eval_anim(camera_desc["z"], t)

        scene.set_camera(
            Camera(
                Vector3(cx, cy, cz),
                camera_desc["width"],
                camera_desc["height"],
                camera_desc["fov"],
            )
        )

    for obj in objects:
        if obj["type"] == "Sphere":
            scene.add_sphere(
                Sphere(
                    Vector3(
                        eval_anim(obj["x"], t),
                        eval_anim(obj["y"], t),
                        eval_anim(obj["z"], t),
                    ),
                    eval_anim(obj["radius"], t),
                    Vector3(*obj["color"]),
                )
            )

        elif obj["type"] == "Light":
            scene.add_light(
                Light(
                    Vector3(
                        eval_anim(obj["x"], t),
                        eval_anim(obj["y"], t),
                        eval_anim(obj["z"], t),
                    ),
                    Vector3(*obj["color"]),
                    eval_anim(obj["intensity"], t),
                )
            )

        elif obj["type"] == "Plane":
            scene.add_plane(
                Plane(
                    Vector3(
                        eval_anim(obj["px"], t),
                        eval_anim(obj["py"], t),
                        eval_anim(obj["pz"], t),
                    ),
                    Vector3(
                        eval_anim(obj["nx"], t),
                        eval_anim(obj["ny"], t),
                        eval_anim(obj["nz"], t),
                    ),
                    Vector3(*obj["color"]),
                )
            )
