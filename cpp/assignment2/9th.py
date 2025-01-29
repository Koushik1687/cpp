import math
a = int(input("enter a digit : "))
b = int(input("enter a digit : "))
c = int(input("enter a digit : "))

print("output: {:.2.f}".format(-b+(math.sqrt(b**2 - 4*a*c))/2*a))
