"""
    Module Image Writer
"""

def save_ppm(filename, image, width, height):
    """
    :param filename: str
    :param image: list
    :param width: int
    :param height: int
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
