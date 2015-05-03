__author__ = 'malin'
import copy


class Interval:
    def __init__(self, x, y):
        self.left = x
        self.right = y

    def __eq__(self, other):
        """
                                    Potrzebny do porownywania elementow
                                    :param other: interval ktory porownujemy z selfem
                                    :return: logiczna wartosc czy self interval jest rowny other
        """
        return other.left == self.left and other.right == self.right

    def __repr__(self):
        """
                                    Reprezentacja w postaci lancucha znakow
                                    :return:obiekt skonwertowany do stringa
        """
        return self.__str__()

    def __hash__(self):
        """
                                    :return ta sama wartosc dla obiektow ktore sa rowne
        """
        return hash(self.__repr__())

    def __str__(self):
        """

                                    :return: Reprezentacja obiektu w postaci stringa
        """
        if self.left == self.right:
            return "[%s]" % self.left
        return "[%s,%s]" % (self.left, self.right)

    def l_degenerate(self):
        """
                                   Utworzenie z przedzialu singletona o lewej wspolrzednej [0,1] - > 0
        """
        self.tmp = self.right
        self.right = self.left

    def r_degenerate(self):
        """
                                   Utworzenie z przedzialu singletona o prawej wspolrzednej [0,1] - > 1
        """
        self.tmp = self.left
        self.left = self.right

    def l_un_degenerate(self):
        """
                                    Powrot z przedzialu zdegnerowanego metoda l_degenerate do normalnego
        """
        self.right = self.tmp

    def r_un_degenerate(self):
        """
                                    Powrot z przedzialu zdegnerowanego metoda l_degenerate do normalnego

        """
        self.left = self.tmp

    @staticmethod
    def is_degenerated(interval):
        """
                                    Sprawdza czy przedzial jest zdegenerowany (singletonem)
                                    :param interval: przedzial do sprawdzenia
                                    :return: wartosc logiczna rownosci lewej i prawej strony przedzialu
        """
        return interval.right == interval.left


class Intervals():
    """
                                    Klasa reprezentujaca zbior przedzialow (K_dim)
    """

    def __init__(self):
        """
                                    :ivar:self.intervals: lista przedzialow
        """
        self.intervals = []

    def __iter__(self):
        """
                                    Iteracja tego obiektu jest tym samym co iteracja na self.intervals
        """
        return iter(self.intervals)

    def append(self, interval):
        """
                                    Dodawanie przedzialow do tego obiektu to kopiowanie nowych interwalow do listy self.intervals
                                    deepcopy uzylem zeby mozna bylo latwo rozszerzyc na dodawanie przedzialow zdegenerowanych
                                    :param interval: przedzial do dodania
        """
        self.intervals.append(copy.deepcopy(interval))

    def __eq__(self, other):
        """
                                    Sprawdzanie rownosci dwoch list intervals sluzy do pisania cos == Intervals
                                    :param other: lista przedzialow do porownania z selfem
                                    :return: czy sa rowne
        """
        if len(self.intervals) != len(other.intervals):
            return False
        for i in range(0, len(self.intervals)):
            if self.intervals[i] != other.intervals[i]:
                return False
        return True

    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        return self.__str__()

    def is_degenerated(self):
        """
                                    Sprawdza czy wszystkie przedzialy sa zdegenerwane
                                    :return: Czy wszystkie przedzialy sa zdegenerowane
        """
        for interval in self.intervals:
            if not Interval.is_degenerated(interval):
                return False
        return True

    def __str__(self):
        """
                                    :return: string w postaci interwalow [a,b] [c,d] ...
        """
        tmp = ""
        for i in self.intervals:
            tmp += str(i)
        return tmp

    @staticmethod
    def n_doubled(intervals):
        """
                                    Sprawdza ile przedzialow jest podwojnych (niezdegenerowanych)
                                    :param intervals: zbior interwalow do sprawdzenia
                                    :return: ilosc nie zdegenerowanych przedzialow
        """
        i = 0
        for interval in intervals.intervals:
            if not Interval.is_degenerated(interval):
                i += 1
        return i
