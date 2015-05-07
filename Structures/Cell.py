class Cell:
    """
                            Cell to uogólnienie sympleksu/kostki/elementu jakiegoś bardziej chorego kompleksu
                            z tego będziemy sobie dziedziczyć do sympleksu i kostki.
                            :ivar id_counter: liczba wszytskich cellow
    """
    id_counter = 0

    def __init__(self, dim: int, label=None):
        """
                                Inicjalizuje zmienne wewnetrzne obiektu
                                :type self.id: int
                                :param dim: wymiar cell'a
                                :param label: domyslnie pusty, nazwa cell'a
                                :type label: str
                                :type dim: int
                                :type self.cofaces: list
                                :type self.faces: list
                                :ivar id: unikatowy numer dla kazdego cella
        """
        self.dim = dim
        self.label = label
        self.faces = set()
        self.cofaces = set()
        self.id = Cell.id_counter
        Cell.id_counter += 1

    def append_coface(self, cell):
        """
                                    Dodaje cell'a 'w gore' w grafie
                                    
                                    :type cell: Cell
                                    :param cell: cell do dodania
        """
        self.cofaces.add(cell)

    def append_face(self, cell):
        """
                                    Dodaje cell'a 'w dol' w grafie
                                    
                                    :type cell: Cell
                                    :param cell: cell do dodania
        """
        self.faces.add(cell)

    def connect(self, cell):
        """
                                    metoda probuje laczyc dwa celle - zwraca True jesli się udalo (wymiary roznia sie o 1)
                                    
                                    :param cell: druga komorka do polaczenia
        """
        if self.dim + 1 == cell.dim:
            self.append_coface(cell)
            cell.append_face(self)
        elif self.dim - 1 == cell.dim:
            self.append_face(cell)
            cell.append_coface(self)
        else:
            return False
        return True

    def __str__(self):
        return "Cell %s: id = %s, dim = %s\n" % (self.label, self.id, self.dim)
