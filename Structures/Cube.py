import copy

from Structures.Interval_for_cubical_complex import Intervals


__author__ = 'malin'


class Cube:
    def __init__(self, dim):
        """
                                    Reprezentuje kostkę
                                    :param dim: wymiar kostki
                                    :ivar self.intervals_list: zbior obiektow Intervals w postaci {intervals1, intervals2,...,intervalsdim} gdzie np
                                    intervalsi = {[a,b]x[c,d]}
        """
        self.intervals_list = []
        self.dim = dim

    def append(self, intervals: Intervals):
        """
                                    Dodawanie do listy interwalow jest tozsame ze skopiowaniem wszystkich danych
                                    :param intervals: przedzial do dodania
        """
        self.intervals_list.append(copy.deepcopy(intervals))

    def __contains__(self, item):
        """
                                    Sprawdza czy przedzial (item) wystepuje w naszej iloscie - sluzy do obslugi cos in Cube
                                    :param item: rzecz do sprawdzenia
                                    :return: czy item sie zawiera czy nie
        """
        for intervals in self.intervals_list:
            if intervals == item:
                return True
        return False

    def __len__(self):
        """
                                    ilosc wszystkich zbiow przedzialow
                                    :return:
        """
        return len(self.intervals_list)

    def __iter__(self):
        """
                                    Do iteracji po naszym obiekcie
        """
        for i in self.intervals_list:
            yield i