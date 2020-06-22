# INPUT
m = float(input("Type a distance in meters: "))
# MATH
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
# OUTPUT
print("\nKm \t \t = \t \t {} \nHm \t \t = \t \t {} \nDam\t \t = \t \t {} \n"
      "Dm \t \t = \t \t {} \ncm \t \t = \t \t {} \nmm \t \t = \t \t {}".format(km, hm, dam, dm, cm, mm))
