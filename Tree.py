__author__ = 'malin'

from Cell import Cell

class Skeleton:
    def __init__(self, dim: int):
        """
        :type self.cellCollection: list
        :type dim: int
        :param dim: wymiar skeletona
        """
        self.dim = dim
        self.cellCollection = []

    def print_all(self):
        """Wypisuje nazwy wszystkich nodow ze spacja po kazdym """
        for cell in self.cellCollection:
            print(cell.label+" ")

    def append(self, cell: Cell):
        """
        :type cell: Cell
        :param cell: Dodaje cell do kolekcji
        """
        self.cellCollection.append(cell)


class Complex:

    def __init__(self):
        """
        :type self.skeletonCollection: list
        """
        self.skeletonCollection = []

    def append(self, skeleton: Skeleton):
        self.skeletonCollection.append(skeleton)

    def print_all(self):
        for skeleton in self.skeletonCollection:
            if skeleton.cellCollection:  # jesli kolekcja jest niepusta
                print("Poziom nr")
                print(skeleton.dim)
                skeleton.print_all()
                print("")






