# INPUT
num1 = int(input('Type the first number: '))
num2 = int(input('Type the second number: '))
num3 = int(input('Type the third number: '))
# OUTPUT
if num1 > num2 and num1 > num3 and num2 > num3:
    print('{} > {} > {}'.format(num1, num2, num3))
if num1 > num2 and num1 > num3 and num3 > num2:
    print('{} > {} > {}'.format(num1, num3, num2))
if num2 > num1 and num2 > num3 and num1 > num3:
    print('{} > {} > {}'.format(num2, num1, num3))
if num2 > num1 and num2 > num3 and num3 > num1:
    print('{} > {} > {}'.format(num2, num3, num1))
if num3 > num1 and num3 > num2 and num1 > num2:
    print('{} > {} > {}'.format(num3, num1, num2))
if num3 > num1 and num3 > num2 and num2 > num1:
    print('{} > {} > {}'.format(num3, num2, num1))