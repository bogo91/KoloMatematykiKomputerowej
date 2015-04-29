__author__ = 'malin'


class Node:

    def __init__(self, N, name="noName"):
        self.N = N
        self.name = name
        self.listup = []
        self.listdown = []

    def append_up(self, node):
        self.listup.append(node)

    def append_down(self, node):
        self.listdown.append(node)


class Level:

    def __init__(self, N):
        self.N = N
        self.nodeCollection = []

    def print_all(self):
        for node in self.nodeCollection:
            print(node.name+" ")

    def append(self,node):
        self.nodeCollection.append(node)


class Structure:

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

class Cubes:
    def __init__(self):
        self.cube_list =[]
    def append(self,cube):
        self.cube_list.append(cube)

    def print(self):
        for cube in self.cube_list:
            print("Cube")
            if cube :
                print(cube)