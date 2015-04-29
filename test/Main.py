__author__ = 'malin'
from Drzewko import Node
from Drzewko import Level
from Drzewko import Structure
from Input import Parser
if __name__ == '__main__':
    # structure = Structure()
    # l0 = Level(0)
    # l1 = Level(1)
    # l2 = Level(2)
    # n0 = Node(0, "0000")
    # n1 = Node(1, "0001")
    # n2 = Node(0, "0010")
    # l0.append(n0)
    # l1.append(n1)
    # l0.append(n2)
    # structure.append(l0)
    # structure.append(l1)
    # structure.append(l2)
    # structure.print_all()
    # print(structure.get_level(l0))
    Parser.parse("(1,1);(2,1);(3,1);(1,2)")
