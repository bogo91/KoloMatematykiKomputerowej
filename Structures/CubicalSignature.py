__author__ = 'malin'


class CubicalSignature:
    def __init__(self, sig):
        self.dim = sum(len(element) for element in sig) - len(sig) 