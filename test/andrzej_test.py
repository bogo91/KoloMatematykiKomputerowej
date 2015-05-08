from Structures.CubicalComplex import CubicalComplex as CC
from Structures.CubicalSignature import CubicalSignature as Sig
import sys
raw=open("../input/andrzej2.txt").read().replace("[","").replace("]","")
test=[Sig([[int(x) for x in interval.split(",")] for interval in line.split("x")]) for line in raw.split("\n") if line !=""]
complex = CC(test);


# Przeglądam cały graf w głąb idąc po kolejnych faceach. Niektóre wierzchołki przegłądam wielokrotnie

stack = [];
for item in complex.cells[complex.dim]:
    stack.append(item);

while(len(stack) != 0):
    current = stack.pop();
    print(current);
    for next in current.faces:
        print("     ", next);
        if len(next.faces) > 0:
            stack.append(next);
