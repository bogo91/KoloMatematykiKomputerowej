import Cube
import Complex

class CubicalComplex(Complex):
    __init__(self, signatures):
        dim=len(signatures[0])
        cubes=[{} for i in range(dim+1)]
        for sig in signatures:
            if not sig in cubes[get_sig_dim(sig)]:
                cubes[get_sig_dim(sig)][sig]=Cube(sig,cubes)
        Complex.__init__(self,cubes.values())




"""
przez sygnature rozumiem [[0,1],[1],[0,1],[0]]
"""


