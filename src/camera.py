"""
    Module Camera
"""

class Camera:
    """
    Class Camera
    
    Attributes
    ----------
    position : Vector3
        position of the camera
    width : float
        width of the camera
    height : float
        height of the camera
    fov : float
        field of view of the camera
    
    """
    def __init__(self, position, width, height, fov):
        self.position = position
        self.width = width
        self.height = height
        self.fov = fov
