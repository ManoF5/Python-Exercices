# INPUT
print("  --Car Rent-- \n")
days = int(input("how many days rented: "))
km = float(input("How many kilometers traveled: "))
# MATH
price = (60 * days) + (km * 0.15)
# OUTPUT
print("Rental price:{}".format(price))
