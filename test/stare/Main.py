__author__ = 'malin'
from Tree import Complex, Skeleton
from Cell import Cell
if __name__ == '__main__':
    print("Zaczynam")
    structure = Complex()
    l0 = Skeleton(0)
    l1 = Skeleton(1)
    l2 = Skeleton(2)
    n0 = Cell(0, "0000")
    n1 = Cell(1, "0001")
    n2 = Cell(0, "0010")
    l0.append(n0)
    l1.append(n1)
    l0.append(n2)
    structure.append(l0)
    structure.append(l1)
    structure.append(l2)
    structure.print_all()
   # Parser.parse("(1,1);(2,1);(3,1);(1,2)")
