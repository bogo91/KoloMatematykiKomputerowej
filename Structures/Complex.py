__author__ = 'ingwarus'

from Structures import Cell
 
class Complex:
    def __init__(self, cells):
        self.cells=cells
        self.dim=len(cells)-1

    def __str__(self):
        s="Complex wymiaru "+str(self.dim)+" zawierajacy:\n"
        for lvl in self.cells:
            for cell in lvl:
                s+=str(cell)
        return s





