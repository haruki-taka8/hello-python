# 003-Fibonacci.py
# Roll a dice and output its die face
# New concept: os, file IO, print(end="")

from random import randint
import os

result = randint(0, 5)
diePath = os.path.join(os.path.dirname(__file__), "dieFace.txt")
with open(diePath) as die:
    dieFile = die.readlines()

for i in range(result*7, result*7+7):
    print (dieFile[i], end="")