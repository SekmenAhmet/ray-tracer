"""
Ecriture d'image au format PPM ASCII (P3).
"""

def save_ppm(filename, image, width, height):
    """
    Ecrit une image RGB au format PPM ASCII (P3).

    Parameters
    ----------
    filename : str
        Chemin du fichier de sortie.
    image : list[list[Vector3]]
        Image sous forme de grille de couleurs.
    width : int
        Largeur de l'image.
    height : int
        Hauteur de l'image.
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
