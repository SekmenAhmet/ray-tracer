"""
Image output in ASCII PPM (P3) and video encoding.
"""

import os
import subprocess

def save_ppm(filename, image, width, height):
    """
    Write an RGB image in ASCII PPM (P3) format.

    Parameters
    ----------
    filename : str
        Output file path.
    image : list[list[Vector3]]
        Image as a grid of colors.
    width : int
        Image width.
    height : int
        Image height.
    """
    with open(filename, 'w') as f:
        f.write('P3\n')
        f.write(f'{width} {height}\n')
        f.write('255\n')

        for row in image:
            for color in row:
                r = int(color.x)
                g = int(color.y)
                b = int(color.z)
                f.write(f'{r} {g} {b}\n')
            f.write('\n')

def build_video_from_ppm(frames_dir, output_path, fps):
    """
    Encode a sequence of PPM frames into an MP4 file using ffmpeg.

    Parameters
    ----------
    frames_dir : str
        Directory containing frame_XXXX.ppm files.
    output_path : str
        Output video file path.
    fps : int
        Frames per second.
    """
    cmd = [
        "ffmpeg",
        "-y",
        "-framerate", str(fps),
        "-i", os.path.join(frames_dir, "frame_%04d.ppm"),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output_path
    ]
    subprocess.run(cmd, check=True)

def next_render_id(base_dir):
    """
    Return the next zero-padded render id for a base directory.

    Parameters
    ----------
    base_dir : str
        Base directory where renders are stored.

    Returns
    -------
    str
        Next render id as a four-digit string.
    """
    os.makedirs(base_dir, exist_ok=True)
    existing = [
        int(d) for d in os.listdir(base_dir)
        if d.isdigit()
    ]
    return f"{(max(existing) + 1) if existing else 1:04d}"
