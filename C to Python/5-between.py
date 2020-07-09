# Do a program that receives a number and tells if this number is between 100 and 200

# INPUT
num = int(input('Type a number: '))
# OUTPUT
if 100 < num and num < 200:
    print('\nThe number {} is between 100 and 200 \n'.format(num))
else:
    print("\nThe number {} isn't between 100 and 200 \n".format(num))