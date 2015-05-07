from Structures.Cell import Cell
__author__ = 'ingwarus'


class Cube(Cell):
    __init__(self, sig, cubes):
        dim=get_sig_dim(sig)
        for each s in get_sig_faces(sig):
            if not s in cubes[dim-1]:
                cubes[dim-1][s]=Cube(s,cubes)
            self.connect(cubes[dim-1][s])
