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
n = int(input('Type a number: '))
factorial = n
# OUTPUT
i = 1
while i < n:
    factorial *=  i
    i += 1
print('{}! = {}'.format(n, factorial))