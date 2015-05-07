from Structures.CubicalComplex import CubicalComplex as CC
from Structures.CubicalSignature import CubicalSignature as Sig
import sys
raw=open("input/ingwarus_test_input1.txt").read().replace("[","").replace("]","")
test=[Sig([[int(x) for x in interval.split(",")] for interval in line.split("x")]) for line in raw.split("\n") if line !=""]
print(CC(test))
