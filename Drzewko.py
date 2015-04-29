__author__ = 'malin'


class Node:

    def __init__(self, N, name="noName"):
        self.N = N
        self.name = name
        self.faces = []
        self.cofaces = []


    def append_coface(self, node):
        self.cofaces.append(node)

    def append_face(self, node):
        self.faces.append(node)


class Level:

    def __init__(self, N):
        self.N = N
        self.nodeCollection = []

    def print_all(self):
        for node in self.nodeCollection:
            print(node.name+" ")

    def append(self,node):
        self.nodeCollection.append(node)


class Complex:

    def __init__(self):
        self.levelCollection = []

    def append(self, level):
        self.levelCollection.append(level)

    def get_level(self, i):
        return self.levelCollection.index(i)

    def print_all(self):
        for level in self.levelCollection:
            if level.nodeCollection:
                print("Poziom nr")
                print(level.N)
                level.print_all()
                print("")






