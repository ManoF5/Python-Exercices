from random import choice
numbers = [0, 1, 2, 3 , 4, 5]
machine_num = choice(numbers)
# COLORS
colors = {
    'CLEAR':'\033[m',
    'GREEN':'\033[1;32m',
    'RED':'\033[1;31m'
    }
# INPUT
print('Try to find the number chosen by the {}machine{}'.format(colors['GREEN'], colors['CLEAR']))
num = int(input('type a number({}0-5{}): '.format(colors['GREEN'], colors['CLEAR'])))
# OUTPUT
if num == machine_num:
    print('\n{}You wins!{}'.format(colors['GREEN'], colors['CLEAR']))
else:
    print('\n{}Machine wins!{}'.format(colors['RED'], colors['CLEAR']))
    print('Better luck next time \n')
