# COLORS
colors = {
    'CLEAR':'\033[m',
    'GREEN':'\033[32m'
    }
# INTRO
print('------------')
print("{}  Car Rent  {}".format(colors['GREEN'], colors['CLEAR']))
print('------------')
# INPUT
days = int(input("\nhow many days rented: "))
km = float(input("How many kilometers traveled: "))
# MATH
price = (60 * days) + (km * 0.15)
# OUTPUT
print("Rental price:{} \n".format(price))
