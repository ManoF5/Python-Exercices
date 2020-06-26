from random import choice
# INPUT
n1 = str(input("First student: "))
n2 = str(input("Second student: "))
n3 = str(input("Third student: "))
n4 = str(input("Fourth student: "))
namelist = [n1, n2, n3, n4]
choice = choice(namelist)
# OUTPUT
print("The chosen student was {}".format(choice))
