# INPUT
r1 = int(input('Enter the length of the first straight: '))
r2 = int(input('Enter the length of the second straight: '))
r3 = int(input('Enter the length of the third straight: '))
# MATH
r = r1 + r2
# OUTPUT
if r > r3:
    print('\nWith these lines it is possible to form a triangle \n')
else:
    print("\nwith these lines it ins't possible to form a triangle \n")