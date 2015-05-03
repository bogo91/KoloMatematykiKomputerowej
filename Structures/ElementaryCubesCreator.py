from Structures.Interval_for_cubical_complex import Intervals, Interval

__author__ = 'malin'


class ElementaryCubesCreator:
    """
                            Zbior przedzialow opartych na kostce podstawowej
    """

    def __init__(self, intervals):
        """
                            Inicjalizuje zmienne oraz wywoluje tworzenie cubów
                            :param intervals:
        """
        max_dim = len(intervals)
        self.cubes = [None] \
                     * (max_dim + 1)  # tworzy tyle pustych cubów ile jest maksymalny wymiar + 1, czyli dla [0,1]x[0,1]x[0,1] utworzy Kn dla n od 0 do 3
        self.cubes[0] = Cube(0)  # zawsze beda istniec punkty
        intervals2 = Intervals()  # zbior interwalow
        """
                            Z listy tworzy obiekty interwalow
        """
        for interval in intervals:
            intervals2.append(Interval(interval[0], interval[1]))
        self.compute_intervals(intervals2)

    def compute_intervals(self, intervals: Intervals):
        """
                            Obliczanie zbiorow kostkowych
                            :param intervals: lista przedzialow do przejzenia
        """
        if intervals.is_degenerated():  # Jeśli wszystkie przedzialy w liscie przedzialow sa zdegenerowane
            if intervals not in self.cubes[0]:  # jesli obiekt jeszcze nie istnieje w zbiorze punktow
                self.cubes[0].append(intervals)
        else:
            dim = Intervals.n_doubled(intervals)  # wymiar to ilosc niezdegerowanych przedzialow
            if self.cubes[dim] is not None:  # jesli istnieje juz cube o takim wymiarze
                if intervals not in self.cubes[dim]:
                    self.cubes[dim].append(intervals)
            else:
                self.cubes[dim] = Cube(dim)  # inicjalizuje cube'a o danym wymiarze
                self.cubes[dim].append(intervals)
            for interval in intervals:
                if not Interval.is_degenerated(interval):  # jesli przedzial nie jest zdegenerowany
                    interval.l_degenerate()  # degenerujemy wzgledem lewej czesci
                    self.compute_intervals(intervals)  # wywolujemy rekurencje
                    interval.l_un_degenerate()  # usuwamy degeneracje
                    interval.r_degenerate()
                    self.compute_intervals(intervals)
                    interval.r_un_degenerate()

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
