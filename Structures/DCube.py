from Structures.Cell import Cell
from Structures.Interval_for_cubical_complex import Interval, Intervals
import copy
__author__ = 'malin'


class DCube(Cell):
    def __init__(self, intervals):
        Cell.__init__(self, len(intervals))
        self.cubelist = [None]*(len(intervals)+1)
        self.cubelist[0]= Cube()
        self.lower = Cube()
        intervals2 = Intervals()
        for interval in intervals:
            intervals2.append(Interval(interval[0], interval[1]))
        intervals = intervals2
        self.compute_intervals(intervals)

    def compute_intervals(self, intervals:Intervals):
        if intervals.is_degenerated():
            if  intervals not in self.cubelist[0]:
                self.cubelist[0].append(intervals)
        else:
            dim = Intervals.n_doubled(intervals)
            if self.cubelist[dim] is not None:
                self.cubelist[dim].append(intervals)
            else:
                self.cubelist[dim] = Cube()
                self.cubelist[dim].append(intervals)
            for interval in intervals:
                if not Interval.is_degenerated(interval):
                    interval.l_degenerate()
                    self.compute_intervals(intervals)
                    interval.l_un_degenerate()
                    interval.r_degenerate()
                    self.compute_intervals(intervals)
                    interval.r_un_degenerate()

class Cube:
    def __init__(self):
        self.points = []

    def append(self,intervals:Intervals):
        self.points.append(copy.deepcopy(intervals))

    def __contains__(self, item):
        for intervals in self.points:
            if intervals.__eq__(item):
                return True
        return False
    def __len__(self):
        return len(self.points)
    def __iter__(self):
        for i in self.points:
            yield i
    def __getitem__(self, item):
        return self.points[item]