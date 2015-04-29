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
        assert isinstance(cell, Cell), "Blad! Dodany obiekt nie jest cellem"
        self.cofaces.add(cell)

    def append_face(self, cell):
        """ Dodaje cell'a 'w dol' w grafie
        :type cell: Cell
        :param cell: node do dodania
        """
        assert isinstance(cell, Cell), "Blad! Dodany obiekt nie jest cellem"
        self.faces.add(cell)

    @staticmethod
    def connect(cell_one, cell_two):

        """metoda laczy dwa celle

        :param cell_one: pierwszy cell
        :param cell_two: drugi cell
        """
        if cell_one.dim + 1 == cell_two.dim:
            cell_one.append_face(cell_two)
            cell_two.append_coface(cell_one)
        elif cell_one.dim - 1 == cell_two.dim:
            cell_one.append_coface(cell_two)
            cell_two.append_face(cell_one)
