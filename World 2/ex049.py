# COLORS
colors = {
    'CLEAN':'\033[m',
    'GREEN':'\033[32m'
}
# INTRO
print('='*22)
print('{} Multiplication Table {}'.format(colors['GREEN'], colors['CLEAN']))
print('='*22)
# INPUT
number = int(input(' Type a number: '))
# OUTPUT
print('='*70)
for tab in range(1, 11):
    print(' {}\t \tx\t \t{}\t \t=\t \t{}'.format(number, tab, (number * tab) ))
print('='*70)
