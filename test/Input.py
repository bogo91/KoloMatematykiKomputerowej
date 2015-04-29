__author__ = 'malin'
from Tree import *

r""" Wejscie z pliku Test1"""


class Parser:
    @staticmethod
    def parse(line):
        file = open("Test1", mode='r')
        cubes = Cubes()
        cubes_list=[]
        for line in file:
            line = "".join(line.split())
            if line == '{':
                cubes = Cubes()
            elif line != '}':
                intervals = line.split("x")
                if intervals != ['']:  # linia nie byla pusta
                    out_intervals = []
                    for interval in intervals:
                        interval = interval.replace("]", '')
                        interval = interval.replace("[", '')
                        out_intervals.append(interval)
                    intervals = out_intervals
                    out_intervals=[]
                    for interval in intervals:
                        interval = interval.split(",")
                        out_intervals.append(interval)
                    intervals = out_intervals
                    cubes.append(intervals)
                   # print(intervals)
                    #print("")
            else:
                cubes_list.append(cubes)
        for cubes in cubes_list:
            if cubes:
                cubes.print()


		

