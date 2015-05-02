__author__ = 'malin'
from Structures.Interval import Interval

class Cube():
    def __init__(self):
        self.dim


class CubicalComplex2d():
    def __init__(self, products):
        self.compute(products)

    def compute(self, products):
        for obj in products:
            self.make_product(obj)

    def make_product(self, obj):
        pointSet = Interval.transform(obj)
        if len(pointSet) == 4:
            print("Mamy pelny w srodku kwadrat!")
        else:
            print("Mamy zbor punktow")
        print("O wspolrzednych")
        for point in pointSet:
            print(point)


