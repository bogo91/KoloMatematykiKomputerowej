__author__ = 'malin'


class CubicalSignature:

    def __init__(self, sig):
        self.sig = sig
        self.dim = sum(len(element) for element in sig) - len(sig)

    def get_faces(self):
        faces = []
        for interval in self.sig:
            face = []
            for i in self.sig:
                if i is interval:
                    face.append(i[0])
                else:
                    face.append(i)
            faces.append(face)
            if len(interval) == 2:
                face = []
                for i in self.sig:
                    if i is interval:
                        face.append(i[1])
                    else:
                        face.append(i)
                faces.append(face)

        return faces
