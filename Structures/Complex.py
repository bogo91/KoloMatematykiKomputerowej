__author__ = 'malin'

from Structures import Cell
 
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
            tmp = "To jest complex z lista zawierajaca :\n\n%s" % "".join(map(lambda x: "poziom %s:\n\n%s" % (x.dim, x),filter(lambda x: x.cellCollection, self.skeletonCollection)))
        else:
            tmp = "To jest complex, ktory jest obecnie pusty"
        return tmp





