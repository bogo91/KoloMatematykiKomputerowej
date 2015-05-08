from Structures.CubicalComplex import CubicalComplex as CC
from Structures.CubicalSignature import CubicalSignature as Sig
import sys
raw=open("../input/andrzej2.txt").read().replace("[","").replace("]","")
test=[Sig([[int(x) for x in interval.split(",")] for interval in line.split("x")]) for line in raw.split("\n") if line !=""]
complex = CC(test);

# sprawdzam czy z istnienia każdego face wynika istnienie odpowiedniego coface

for level in complex.cells:
    for item in level:
        for face in item.faces:
            if item in face.cofaces == False:
                print("!!!")
            else:
                print("OK");


