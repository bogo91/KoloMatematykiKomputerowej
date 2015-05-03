from Structures.Cell import Cell
__author__ = 'malin'


class Cube(Cell):
    def __init__(self, sig, cubes):
        """
                                        Sig ma postac [0,1],[1],[0,1],[0]
        """
        super().__init__(len(sig), sig)



"""
dim=get_sig_dim(sig)
for each s in get_sig_faces(sig):
    if not s in cubes[dim-1]:
        cubes[dim-1][s]=Cube(s,cubes)
    self.connect(cubes[dim-1][s]
"""
