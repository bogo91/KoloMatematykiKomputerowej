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
        tmp = "Skeleton "
        tmp += "wymiaru {wymiar}".format(wymiar=self.dim)
        if self.cellCollection:
            tmp += " z nastepujacymi cellami : \n"
            for cell in self.cellCollection:
                tmp += str(cell)
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
        tmp = "To jest complex "
        if self.skeletonCollection:
            tmp +="z lista zawierajaca :\n\n"
            for skeleton in self.skeletonCollection:
                if skeleton.cellCollection:
                    tmp+="poziom {poziom}:\n".format(poziom=skeleton.dim)
                    tmp+=str(skeleton)+"\n"
        else:
            tmp+="ktory jest obecnie pusty "
        return tmp





