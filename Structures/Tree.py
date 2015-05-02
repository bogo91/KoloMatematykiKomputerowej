__author__ = 'malin'

from Structures import Cell


class Skeleton:
    def __init__(self, dim: int):
        """
        :type self.cellCollection: list
        :type dim: int
        :param dim: wymiar skeletona
        """
        self.dim = dim
        self.cellCollection = []

    def __str__(self):
        if self.cellCollection:
            tmp = "Skeleton wymiaru %d z nastepujacymi cellami : \n %s" % (self.dim, " ".join(self.cellCollection))
        else:
            tmp = "Skeleton wymiaru %d" % self.dim
        return tmp


    def append(self, cell: Cell):
        """
        :type cell: Cell
        :param cell: Dodaje cell do kolekcji
        """
        self.cellCollection.append(cell)


class Complex:
    def __init__(self, list):
        """
        :type self.skeletonCollection: list
        """
        self.skeletonCollection = list

    def append(self, skeleton: Skeleton):
        self.skeletonCollection.append(skeleton)

    def __str__(self):
        if self.skeletonCollection:
            tmp = "To jest complex z lista zawierajaca :\n\n%s" % "".join(map(lambda x: "poziom {poziom}:\n%s\n" % x, filter(lambda x: x.cellCollection, self.skeletonCollection)))
        else:
            tmp = "To jest complex, ktory jest obecnie pusty"
        return tmp





