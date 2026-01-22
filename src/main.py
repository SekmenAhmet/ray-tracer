"""
Command-line entry point for rendering scenes to images or videos.
"""

import math
import os
import shutil
import sys
from concurrent.futures import ProcessPoolExecutor

from image_writer import next_render_id, save_ppm, build_video_from_ppm
from init_fs import init_filesystem
from renderer import Renderer
from scene import Scene
from sceneLoader import SceneLoader
from scene_builder import build_scene_at_t

def render_frame_to_ppm(frame_index, frame_count, camera_desc, objects, frames_dir):
    """
    Render a single video frame to a PPM file.

    Parameters
    ----------
    frame_index : int
        Index of the frame to render.
    frame_count : int
        Total number of frames.
    camera_desc : dict
        Camera description parsed from the scene file.
    objects : list[dict]
        Object descriptions parsed from the scene file.
    frames_dir : str
        Output directory for PPM frames.
    """
    scene = Scene()
    t = frame_index / (frame_count - 1) if frame_count > 1 else 0.0
    build_scene_at_t(scene, camera_desc, objects, t)

    renderer = Renderer(scene)
    image = renderer.render()
    save_ppm(
        f"{frames_dir}/frame_{frame_index:04d}.ppm",
        image,
        scene.camera.width,
        scene.camera.height
    )

def render_image(camera_desc, objects, out_dir):
    """
    Render a single image and write it as PPM.

    Parameters
    ----------
    camera_desc : dict
        Camera description parsed from the scene file.
    objects : list[dict]
        Object descriptions parsed from the scene file.
    out_dir : str
        Output directory for the rendered image.
    """
    scene = Scene()
    build_scene_at_t(scene, camera_desc, objects, 0.0)

    renderer = Renderer(scene)
    image = renderer.render()
    save_ppm(
        f"{out_dir}/render.ppm",
        image,
        scene.camera.width,
        scene.camera.height
    )

def render_video(header, camera_desc, objects, out_dir):
    """
    Render a sequence of frames and encode them into a video.

    Parameters
    ----------
    header : Header
        Parsed header describing render type and timing.
    camera_desc : dict
        Camera description parsed from the scene file.
    objects : list[dict]
        Object descriptions parsed from the scene file.
    out_dir : str
        Output directory for frames and final video.
    """
    frames_dir = f"{out_dir}/frames"
    os.makedirs(frames_dir, exist_ok=True)

    frame_count = max(1, int(math.ceil(header.fps * header.duration)))
    max_workers = min(frame_count, os.cpu_count() or 1)

    if max_workers <= 1:
        for i in range(frame_count):
            render_frame_to_ppm(i, frame_count, camera_desc, objects, frames_dir)
    else:
        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            futures = [
                executor.submit(
                    render_frame_to_ppm,
                    i,
                    frame_count,
                    camera_desc,
                    objects,
                    frames_dir,
                )
                for i in range(frame_count)
            ]
            for future in futures:
                future.result()

    build_video_from_ppm(
        frames_dir,
        f"{out_dir}/out.mp4",
        header.fps
    )

    shutil.rmtree(frames_dir)

def main():
    """
    Initialize the filesystem, parse the scene, and render output.
    """
    init_filesystem()

    scene_path = sys.argv[1] if len(sys.argv) > 1 else "scene/scene1.txt"
    loader = SceneLoader(scene_path)
    header, camera_desc, objects = loader.parse()

    if header.type == "image":
        render_id = next_render_id("output/images")
        out_dir = f"output/images/{render_id}"
        os.makedirs(out_dir, exist_ok=True)
        render_image(camera_desc, objects, out_dir)

    elif header.type == "video":
        render_id = next_render_id("output/video")
        out_dir = f"output/video/{render_id}"
        os.makedirs(out_dir, exist_ok=True)
        render_video(header, camera_desc, objects, out_dir)

if __name__ == "__main__":
    main()
