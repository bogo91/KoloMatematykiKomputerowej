from Structures.Complex import Complex
from Structores.Complex import Cube
__author__ = 'ingwarus'


class CubicalComplex(Complex):
    __init__(self, signatures):
        dim=len(signatures[0])
        cubes=[{} for i in range(dim+1)]
        for sig in signatures:
            if not sig in cubes[get_sig_dim(sig)]:
                cubes[get_sig_dim(sig)][sig]=Cube(sig,cubes)
        Complex.__init__([x.values() for x in self.cubes])
