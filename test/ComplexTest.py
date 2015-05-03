from Structures.DCube import DCube

__author__ = 'malin'

# c = CubicalComplex2d([([0, 0], [2, 3]), ([0, 1], [3, 3]), ([0, 1], [2, 2]), ([1, 1], [2, 3])])
c = DCube([[0, 1], [0, 1], [0, 1],[0,1]])
print("Wypisuje punkty")
i=0
for ob in c.cubelist:
    print("Dim =%s"%i)
    for o in ob:
        print(o)
    i+=1