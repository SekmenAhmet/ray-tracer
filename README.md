# Ray Tracer (Python)

Small educational ray tracer that loads a text scene, traces rays against
spheres and planes, and writes either a PPM image or an MP4 video.

## Goals

- Perspective camera
- Ray-sphere and ray-plane intersections
- Phong lighting with hard shadows
- 2x2 anti-aliasing

## Requirements

- Python 3.8+
- ffmpeg (only required for video output)

## Run

From the project root:

```bash
python src/main.py
```

To render a specific scene:

```bash
python src/main.py scene/scene2.txt
```

Outputs are written under `output/`:

- Images: `output/images/<id>/render.ppm`
- Videos: `output/video/<id>/out.mp4`

The render id is a zero-padded directory name (e.g., `0001`, `0002`).

## Scene format

Each non-empty line defines an element:

```
Header image
Camera x y z width height fov
Light x y z r g b intensity
Sphere x y z radius r g b
Plane px py pz nx ny nz r g b
```

For video renders:

```
Header video <fps> duration=<seconds>
```

Numeric values can be animated by using a range: `(start,end)`. The value is
linearly interpolated over the video duration.

Example:

```
Header video 30 duration=2.5
Camera (-1.5,1.5) 1 3.5 960 540 60
Light 0 8 -6 255 255 255 0.25
Sphere 0 0 -6 1.2 220 70 70
```

Scenes are available in `scene/` (e.g., `scene/scene1.txt`).

## View the result

PPM output is ASCII (P3). You can open it with a PPM viewer or convert it:

```bash
convert output/images/0001/render.ppm output/images/0001/render.png
```

## Code layout

- `src/main.py` : entry point, loads the scene and dispatches render type
- `src/renderer.py` : render loop, primary rays, lighting
- `src/vector.py` : 3D vector operations
- `src/ray.py` : ray definition
- `src/sphere.py` : ray-sphere intersection
- `src/plane.py` : ray-plane intersection
- `src/camera.py` : perspective camera
- `src/light.py` : point light
- `src/scene.py` : scene container (camera, objects, lights)
- `src/sceneLoader.py` : scene file parsing
- `src/scene_builder.py` : scene instantiation at time t
- `src/headers.py` : header parsing and validation
- `src/image_writer.py` : PPM output and video encoding
- `src/init_fs.py` : creates `output/` and `scene/` folders

## Known limitations

- Geometry limited to spheres and planes
- No reflections, textures, or anti-aliasing beyond 2x2
- Simple lighting and hard shadows
