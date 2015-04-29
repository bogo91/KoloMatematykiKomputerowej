__author__ = 'malin'


class Cell:
    """
        :ivar sum: suma wszytskich cellow
    """
    sum = 0

    def __init__(self, dim: int, label: str=None):
        """ Inicjalizuje zmienne wewnetrzne obiektu

        :type self.id: int
        :param dim: wymiar node'a
        :param label: domyslnie pusty, nazwa cell'a
        :type label: str
        :type dim: int
        :type self.cofaces: list
        :type self.faces: list
        :ivar id: unikatowy numer lda kazdego cella 
        """
        self.dim = dim
        self.label = label
        self.faces = set()
        self.cofaces = set()
        self.id = Cell.sum
        Cell.sum += 1

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
            self.faces.add(cell)
            cell.append_coface(self)

