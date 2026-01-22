"""
Scene header definition and validation.
"""


class Header:
    """
    Scene header settings.

    Attributes
    ----------
    type : str
        Output type ("image" or "video").
    fps : int or None
        Frames per second for video output.
    duration : float
        Duration in seconds for video output.
    """
    def __init__(self):
        """
        Initialize header defaults.
        """
        self.type = "image"
        self.fps = None
        self.duration = 1.0

    def validate(self):
        """
        Validate header values and normalize fields.
        """
        if(self.type not in ("image", "video")):
            raise ValueError("Le type d'output doit etre une image ou une vidéo")

        if self.duration <= 0:
            raise ValueError("La duration doit etre > 0")

        if(self.type == "video"):
            if(self.fps == None):
                raise ValueError("Le nombre de fps est obligatoire pour une video")
            if not(1 <= self.fps <=60):
                raise ValueError("fps doit etre entre 1 et 60")

        else:
            self.fps = None
        
