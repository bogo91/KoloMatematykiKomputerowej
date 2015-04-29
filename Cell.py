__author__ = 'malin'

class Cell:
    def __init__(self, dim: int, name: str=""):
        """ Inicjalizuje zmienne wewnetrzne obiektu

        :param dim: wymiar node'a
        :param name: domyslnie pusty, nazwa cell'a
        :type name: str
        :type dim: int
        :type self.cofaces: list
        :type self.faces: list
        """
        self.dim = dim
        self.name = name
        self.faces = set()
        self.cofaces = set()

    def append_coface(self, cell):
        """Dodaje cell'a 'w gore' w grafie
        :type cell: Cell
        :param cell: node do dodania
        """
        if cell not in self.cofaces:
            assert isinstance(cell, Cell), "Blad! Dodany obiekt nie jest cellem"
            self.cofaces.add(cell)
            cell.append_face(self)

    def append_face(self, cell):
        """ Dodaje cell'a 'w dol' w grafie
        :type cell: Cell
        :param cell: node do dodania
        """
        if cell not in self.faces:
            assert isinstance(cell, Cell), "Blad! Dodany obiekt nie jest cellem"
            self.faces.add(cell.append_coface(cell))
            cell.append_coface(self)

