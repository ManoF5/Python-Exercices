# INPUT
something = input("Type something: ")
# OUTPUT
print("Primitive type:", type(something))
print("Only have spaces:", something.isspace())
print("Is a number:", something.isnumeric())
print("Is alphabetic:", something.isalpha())
print("Is alphanumeric:", something.isalnum())
print("Is in upper case:", something.isupper())
print("Is in lowercase:", something.islower())
print("Is capitalized:", something.istitle())
