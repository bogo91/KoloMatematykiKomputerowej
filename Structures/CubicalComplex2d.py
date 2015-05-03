from Structures.Interval_for_cubical_complex import Interval

__author__ = 'malin'


class Cube():
    def __init__(self):
        self.dim


class CubicalComplex2d():
    def __init__(self, products):
        self.compute(products)

    def compute(self, products):
        """
                                    :param products: lista interwalow
        """
        for interval in products:
            self.make_product(interval)

    def make_product(self, obj):
        """
                                    :param obj: interwal w postaci tekstowej
        """
        pointSet = Interval.transform(obj)
        if len(pointSet) == 4:
            print("Mamy pelny w srodku kwadrat!")
        else:
            print("Mamy zbor punktow")
        print("O wspolrzednych")
        for point in pointSet:
            print(point)
