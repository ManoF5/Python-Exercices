# INPUT
import math
opposite = float(input("Opposite side length: "))
adjacent = float(input("Adjacent side length: "))
# MATH
hypotenuse = math.sqrt(opposite**2 + adjacent**2)
# OUTPUT
print("hypotenuse² \t \t = \t \t opposite² \t \t + \t \t adjacent²")
print("{}          \t \t = \t \t {}       \t \t + \t \t {}".format((hypotenuse**2), opposite, adjacent))
print("{}".format(hypotenuse))
