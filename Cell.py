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
        self.faces = []
        self.cofaces = []

    def append_coface(self, cell):
        """Dodaje cell'a 'w gore' w grafie
        :type cell: Cell
        :param cell: node do dodania
        """
        assert isinstance(cell, object), "Blad! Dodany obiekt nie jest nodem"
        self.cofaces.append(cell)

    def append_face(self, cell):
        """ Dodaje cell'a 'w dol' w grafie
        :type cell: Cell
        :param cell: node do dodania
        """
        assert isinstance(cell, object), "Blad! Dodany obiekt nie jest nodem"
        self.faces.append(cell)

