# Ray Tracer (Python)

Mini ray tracer educatif qui charge une scene texte, trace des rayons
sur des spheres et ecrit une image PPM.

## Objectif

Ce projet illustre les bases du rendu par lancer de rayons:
camera perspective, intersection rayon-sphere, eclairage de type Phong
et ombres simples.

## Prerequis

- Python 3.8+

## Installation

Aucune dependance externe.

## Lancer le rendu

Depuis la racine du projet:

```bash
python src/main.py
```

Le rendu est ecrit dans `output/image.ppm`.

## Format de scene

Chaque ligne du fichier de scene decrit un element:

```
Camera x y z width height fov
Light x y z r g b intensity
Sphere x y z radius r g b
```

Exemple:

```
Camera 0 0 0 800 600 90
Light 5 5 0 255 255 255 1
Sphere 0 0 -5 1 255 0 0
```

Scenes disponibles dans `scene/` (ex: `scene/scene1.txt`).

## Notions (resume)

- Vecteur 3D: addition, soustraction, normalisation, produit scalaire.
- Rayon: origine + direction, point calcule par `point_at(t)`.
- Camera: determine le plan image et le champ de vision (FOV).
- Intersection rayon-sphere: resolution d'une equation quadratique,
  selection de la plus petite racine positive.
- Eclairage: composantes ambiante + diffuse (Lambert) + speculaire (Phong),
  ombres via un rayon de test vers la lumiere.
- Format PPM: sortie ASCII (P3), valeurs RGB dans [0, 255].

## Organisation du code

- `src/main.py` : point d'entree, charge la scene et lance le rendu.
- `src/renderer.py` : boucle de rendu, rays primaires, eclairage.
- `src/vector.py` : operations vectorielles 3D.
- `src/ray.py` : definition d'un rayon.
- `src/sphere.py` : intersection rayon-sphere.
- `src/camera.py` : camera perspective.
- `src/light.py` : lumiere ponctuelle.
- `src/scene.py` : conteneur de scene (camera, objets, lumieres).
- `src/sceneLoader.py` : parsing du fichier de scene.
- `src/image_writer.py` : ecriture PPM.
- `src/init_fs.py` : creation des dossiers `output/` et `scene/`.

## Visualiser l'image

Le fichier `output/image.ppm` est un PPM ASCII. Vous pouvez:

- l'ouvrir avec un viewer compatible PPM
- le convertir en PNG avec ImageMagick:

```bash
convert output/image.ppm output/image.png
```

## Limites connues

- Geometrie limitee aux spheres.
- Pas de reflexions, textures, ni anti-aliasing.
- Eclairage simple et ombres dures.
