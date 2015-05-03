__author__ = 'malin'


class CubicalSignature:
    def __init__(self, sig):
        self.dim = CubicalSignature.degenerated_count(sig)

    @staticmethod
    def degenerated_count(sig):
        i = 0
        for element in sig:
            if len(element) == 2:
                i += 1
        return i