"""
Parse scene description files into renderable data.
"""

from headers import Header


class SceneLoader:
    """
    Load a scene text file into header, camera, and object descriptions.
    """
    def __init__(self, filename) -> None:
        """
        Initialize the loader with a scene file path.

        Parameters
        ----------
        filename : str
            Path to the scene file.
        """
        self.filename = filename
        self.header = Header()
        self.header_parsed = False
        self.camera_desc = None
        self.objects = []

    def parse(self):
        """
        Parse the scene file and return header, camera, and object data.

        Returns
        -------
        tuple[Header, dict, list[dict]]
            Parsed header, camera description, and objects.
        """
        parsers = {
            "Header": self.parse_header,
            "Camera": self.parse_camera,
            "Light": self.parse_light,
            "Sphere": self.parse_sphere,
            "Plane": self.parse_plane,
        }

        with open(self.filename, "r", encoding="utf-8") as file:
            for lineno, f in enumerate(file, start=1):
                line = f.strip()
                if not line or line.startswith("#"):
                    continue

                words = line.split()
                key = words[0]

                if key != "Header" and not self.header_parsed:
                    raise ValueError(f"Ligne {lineno}: Le header doit être défini avant les objets")

                if key == "Header" and self.header_parsed:
                    raise ValueError(f"Ligne {lineno}: Le header ne peut être défini qu'une seule fois")

                if key not in parsers:
                    raise ValueError(f"Ligne {lineno}: Type inconnu dans la scene: {key}")

                parsers[key](words, lineno)

        self.header.validate()
        if self.camera_desc is None:
            raise ValueError("Aucune camera definie dans la scene")
        return self.header, self.camera_desc, self.objects

    @staticmethod
    def parse_anim_value(token):
        """
        Parse a numeric token, supporting animated ranges like "(a,b)".

        Parameters
        ----------
        token : str
            Token to parse.

        Returns
        -------
        float or tuple[float, float]
            Parsed value or (start, end) range.
        """
        token = token.strip()
        if "=" in token:
            token = token.split("=", 1)[1]
        if token.startswith("(") and token.endswith(")"):
            a, b = token[1:-1].split(",")
            return (float(a), float(b))
        return float(token)

    def parse_header(self, words, lineno):
        """
        Parse a Header line and update the header state.

        Parameters
        ----------
        words : list[str]
            Tokenized line.
        lineno : int
            Line number for error reporting.
        """
        if len(words) < 2:
            raise ValueError(f"Ligne {lineno}: Header incomplet")

        self.header.type = words[1]

        if self.header.type == "video":
            if len(words) < 3:
                raise ValueError(f"Ligne {lineno}: FPS manquant pour la vidéo")
            self.header.fps = int(words[2])


        
        if len(words) >= 4 and words[3].startswith("duration="):
            try:
                self.header.duration = float(words[3].split("=")[1])
            except ValueError:
                raise ValueError(f"Ligne {lineno}: duration invalide")

        self.header_parsed = True

    def parse_camera(self, words, lineno):
        """
        Parse a Camera line into a camera description dict.

        Parameters
        ----------
        words : list[str]
            Tokenized line.
        lineno : int
            Line number for error reporting.
        """
        if len(words) != 7:
            raise ValueError(f"Ligne {lineno}: Camera attend 6 paramètres")

        try:
            x = self.parse_anim_value(words[1])
            y = self.parse_anim_value(words[2])
            z = self.parse_anim_value(words[3])
            w = int(words[4])
            h = int(words[5])
            fov = float(words[6])
        except ValueError:
            raise ValueError(f"Ligne {lineno}: Paramètres invalides pour Camera")

        self.camera_desc = {
            "type": "Camera",
            "x": x,
            "y": y,
            "z": z,
            "width": w,
            "height": h,
            "fov": fov,
        }

    def parse_light(self, words, lineno):
        """
        Parse a Light line into an object description.

        Parameters
        ----------
        words : list[str]
            Tokenized line.
        lineno : int
            Line number for error reporting.
        """
        if len(words) != 8:
            raise ValueError(f"Ligne {lineno}: Light attend 7 paramètres")

        try:
            x = self.parse_anim_value(words[1])
            y = self.parse_anim_value(words[2])
            z = self.parse_anim_value(words[3])
            r = int(words[4])
            g = int(words[5])
            b = int(words[6])
            intensity = self.parse_anim_value(words[7])
        except ValueError:
            raise ValueError(f"Ligne {lineno}: Paramètres invalides pour Light")

        self.objects.append({
            "type": "Light",
            "x": x,
            "y": y,
            "z": z,
            "color": (r, g, b),
            "intensity": intensity,
        })

    def parse_sphere(self, words, lineno):
        """
        Parse a Sphere line into an object description.

        Parameters
        ----------
        words : list[str]
            Tokenized line.
        lineno : int
            Line number for error reporting.
        """
        if len(words) != 8:
            raise ValueError(f"Ligne {lineno}: Sphere attend 7 paramètres")

        try:
            x = self.parse_anim_value(words[1])
            y = self.parse_anim_value(words[2])
            z = self.parse_anim_value(words[3])
            radius = self.parse_anim_value(words[4])
            r = int(words[5])
            g = int(words[6])
            b = int(words[7])
        except ValueError:
            raise ValueError(f"Ligne {lineno}: Paramètres invalides pour Sphere")

        self.objects.append({
            "type": "Sphere",
            "x": x,
            "y": y,
            "z": z,
            "radius": radius,
            "color": (r, g, b),
        })

    def parse_plane(self, words, lineno):
        """
        Parse a Plane line into an object description.

        Parameters
        ----------
        words : list[str]
            Tokenized line.
        lineno : int
            Line number for error reporting.
        """
        if len(words) != 10:
            raise ValueError(f"Ligne {lineno}: Plane attend 9 paramètres")

        try:
            px = self.parse_anim_value(words[1])
            py = self.parse_anim_value(words[2])
            pz = self.parse_anim_value(words[3])
            nx = self.parse_anim_value(words[4])
            ny = self.parse_anim_value(words[5])
            nz = self.parse_anim_value(words[6])
            r = int(words[7])
            g = int(words[8])
            b = int(words[9])
        except ValueError:
            raise ValueError(f"Ligne {lineno}: Paramètres invalides pour Plane")

        self.objects.append({
            "type": "Plane",
            "px": px,
            "py": py,
            "pz": pz,
            "nx": nx,
            "ny": ny,
            "nz": nz,
            "color": (r, g, b),
        })
