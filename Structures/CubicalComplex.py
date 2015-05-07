from Structures.Complex import Complex
from Structures.Cube import Cube


class CubicalComplex(Complex):
    def __init__(self, signatures):
        dim=signatures[0].get_len()
        cubes=[{} for i in range(dim+1)]
        for sig in signatures:
            sig_dim=sig.get_dim()
            if not sig in cubes[sig_dim]:
                cubes[sig_dim][sig]=Cube(sig_dim,sig,cubes)
        Complex.__init__(self,[x.values() for x in cubes])
