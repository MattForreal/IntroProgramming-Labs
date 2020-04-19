

n = int(input("Please enter a value for n: "))
total=0
for i in range(1,n):
        total += (-1)**(i+1)*((1.0/(i+i+1)))
print()
value = 4*(1-total)
print(value)
print()
print("Compare that to the actual value of pi below.")
print()
import math
from math import pi
print (pi)
