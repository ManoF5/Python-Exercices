# Area of the wall and amount of ink to paint this wall
# INPUT
width = float(input("Type the wall width: "))
height = float(input("Type the wall height: "))
# MATH
area = width * height
ink = area / 2
# OUTPUT
print("\nArea of the wall:{:.2f}m² \n"
      "Amount of ink necessary to paint this wall:{:.2f}l".format(area, ink))
