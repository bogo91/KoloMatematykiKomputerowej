__author__ = 'malin'


class Cube():
    def __init__(self):
        self.dim


class CubicalComplex():
    def __init__(self, products):
        self.compute(products)

    def compute(self, products):
        for obj in products:
            self.make_product(obj)

    def make_product(self, obj):
        print("Tworze produkt z ")
        for o in obj:
            p = Point.transform(o)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def transform(obj):
        print(obj)

    def __str__(self):
        return "({x},{y})".format(x=self.x,y=self.y)
    @staticmethod
    def cross(pointA,pointB):
        return Point(pointA.x,pointB.y),