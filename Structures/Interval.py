__author__ = 'malin'


class Interval():
    def __init__(self, x, y):
        self.left = x
        self.right = y

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
        return "(%s,%s)" % (self.left, self.right)

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
        return "(%s,%s)" % (self.left, self.right)

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
