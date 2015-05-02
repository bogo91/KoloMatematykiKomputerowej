__author__ = 'malin'


class Interval():
    def __init__(self, x, y):
        self.left = x
        self.right = y

    def __eq__(self, other):
        return other.left == self.left and other.right == self.right

    def __repr__(self):
        return "({left},{right})".format(left=self.left, right=self.right)

    def __hash__(self):
        return hash(self.__repr__())

    @staticmethod
    def transform(obj):
        intervallist = []
        for interval in obj:
            interval = Interval(interval[0], interval[1])
            intervallist.append(interval)
        pointList = Interval.cross(intervallist[0], intervallist[1])
        return pointList

    def __str__(self):
        return "({x},{y})".format(x=self.left, y=self.right)

    @staticmethod
    def cross(intervalA, intervalB):
        out = set()
        out.add(Interval(intervalA.left, intervalB.right))
        out.add(Interval(intervalA.left, intervalB.left))
        out.add(Interval(intervalA.right, intervalB.left))
        out.add(Interval(intervalA.right, intervalB.right))
        return out
