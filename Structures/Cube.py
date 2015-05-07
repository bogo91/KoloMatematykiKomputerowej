import pdb
from Structures.Cell import Cell


class Cube(Cell):
    def __init__(self, dim,sig, cubes):
        Cell.__init__(self,sig.get_dim())
        self.signature=sig
        #pdb.set_trace()
        for s in sig.get_faces():
            if not s in cubes[dim-1]:
                cubes[dim-1][s]=Cube(dim-1,s,cubes)
            self.connect(cubes[dim-1][s])
    def __str__(self):
        return "Cube %s: id = %s, dim = %s\n" % (self.signature, self.id, self.dim)
