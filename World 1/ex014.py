# INPUT
print("    ---Temperature Converter--- \n")
celsius = float(input("Type the temperature in degrees celsius:"))
# MATH
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15
# OUTPUT
print("Celsius:\t \t{}°C \n"
      "Fahrenheit:\t \t{}°F \n"
      "Kelvin: \t \t{}K \n".format(celsius, fahrenheit, kelvin))
