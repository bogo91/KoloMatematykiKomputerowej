from Structures.CubesCreator.ElementaryCubesCreator import ElementaryCubesCreator

__author__ = 'malin'

c = ElementaryCubesCreator([[0, 1], [0, 1], [0, 1]])
print("Wypisuje przedzialy")
for ob in c.cubes:
    print("Dim =%s" % ob.dim)
    for o in ob:
        print(o)

c = ElementaryCubesCreator([[0, 1], [0, 1]])
print("Wypisuje przedzialy")
for ob in c.cubes:
    print("Dim =%s" % ob.dim)
    for o in ob:
        print(o)

c = ElementaryCubesCreator([[0, 1], [0, 1], [0, 1], [0, 1]])
print("Wypisuje przedzialy")
for ob in c.cubes:
    print("Dim =%s" % ob.dim)
    for o in ob:
        print(o)
