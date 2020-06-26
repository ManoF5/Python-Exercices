from math import radians, sin, cos, tan
# INPUT
angle = float(input("Type a angle: "))
# MATH
sine = sin(radians(angle))
cosine = cos(radians(angle))
tangent = tan(radians(angle))
# OUTPUT
print("\nThe {}-degree angle has: \n"
      "Sine:   \t \t{:.2f} \n"
      "Cosine: \t \t{:.2f} \n"
      "Tangent:\t \t{:.2f} \n".format(angle, sine, cosine, tangent))
