# COLOR
colors = {
    'clean':'\033[m',     # clear the colors
    'blue':'\033[1;34m'   # bold blue
}         
#INTRO
print('-------------------------')
print("{}  Temperature Converter  {} ".format(colors['blue'], colors['clean']))
print('-------------------------')
# INPUT
celsius = float(input("\nType the temperature in degrees celsius:"))
# MATH
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15
# OUTPUT
print("Celsius:\t \t{}°C \n"
      "Fahrenheit:\t \t{}°F \n"
      "Kelvin: \t \t{}K \n".format(celsius, fahrenheit, kelvin))
