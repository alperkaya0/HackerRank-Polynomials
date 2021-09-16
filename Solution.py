import numpy


coeff = input().split(" ")
x = int(input())


for y in range(len(coeff)):
    coeff[y] = float(coeff[y])

print(numpy.polyval(coeff,x))
