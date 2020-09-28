from math import factorial
# COLORS
colors = {
    'CLEAN':'\033[m',
    'GREEN':'\033[32m'
    }
# INTRO
print('='*23)
print('{} Factorial Calculation {}'.format(colors['GREEN'], colors['CLEAN']))
print('='*23)
# INPUT
num = int(input('Type a number: '))
fac = factorial(num)
# OUTPUT
print('{}! = {}'.format(num, fac))