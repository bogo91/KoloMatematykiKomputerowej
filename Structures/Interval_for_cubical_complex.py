__author__ = 'malin'
import copy


class Interval():
    count = 0

    def __init__(self, x, y):
        self.left = x
        self.right = y
    def __len__(self):
        if self.is_degenerated(self):
            return 1
        else:
            return 2
    def __eq__(self, other):
        """
                                    Potrzebny do porownywania elementow w secie
                                    :param other: interval ktory porownujemy z selfem
                                    :return: logiczna wartosc czy self interval jest rowny other
        """
        return other.left == self.left and other.right == self.right

    def __repr__(self):
        """
                                    Potrzebny do porownywania i dodawania elementow w secie
                                    :return:obiekt skonwertowany do stringa
        """
        return self.__str__()

    def __hash__(self):
        """
                                    Potrzebny do porownywania i dodawania elementow w secie
        """
        return hash(self.__repr__())

    @staticmethod
    def transform(obj):
        """
                                    Zamienia
                                    :param obj: obiekt do transofmracji
                                    :return: liste punktow utworzonych z obj
        """
        intervallist = []
        for interval in obj:
            interval = Interval(interval[0], interval[1])
            intervallist.append(interval)
        pointList = Interval.cross(intervallist[0], intervallist[1])
        return pointList

    def __str__(self):
        if (self.left == self.right):
            return "[%s]" % self.left
        return "[%s,%s]" % (self.left, self.right)

    @staticmethod
    def cross(intervalA, intervalB):
        """
                                    :return: zbior punktow utworzonych z interwalow A i B
                                    Przyklad :
                                        [0, 0], [2, 3] zwroci : (0, 2), (0, 3)
                                        [0, 1], [2, 3] zwroci : (0, 2), (0, 3), (1, 2), (1, 3)
        """
        out = set()
        out.add(Interval(intervalA.left, intervalB.right))
        out.add(Interval(intervalA.left, intervalB.left))
        out.add(Interval(intervalA.right, intervalB.left))
        out.add(Interval(intervalA.right, intervalB.right))
        return out

    def l_degenerate(self):
        self.tmp = self.right
        self.right = self.left

    def r_degenerate(self):
        self.tmp = self.left
        self.left = self.right

    def l_un_degenerate(self):
        self.right = self.tmp

    def r_un_degenerate(self):
        self.left = self.tmp

    @staticmethod
    def is_degenerated(interval):
        return interval.right == interval.left


class Intervals():
    def __init__(self):
        self.intervals = []

    def __iter__(self):
        return iter(self.intervals)

    def append(self, interval):
        self.intervals.append(copy.deepcopy(interval))

    def __eq__(self, other):
        if len(self.intervals) != len(other.intervals):
            return False
        for i in range(0, len(self.intervals)):
            if self.intervals[i] != other.intervals[i]:
                return False
        return True

    def __len__(self):
        return len(self.intervals)

    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        return self.__str__()

    def is_degenerated(self):
        for interval in self.intervals:
            if not Interval.is_degenerated(interval):
                return False
        return True

    def __str__(self):
        tmp = ""
        for i in self.intervals:
            tmp += str(i)
        return tmp
    @staticmethod
    def n_doubled(intervals):
        i=0
        for interval in intervals.intervals:
            if len(interval)== 2:
                i+=1
        return i
