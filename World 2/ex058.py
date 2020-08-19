from random import randint
machine_num = randint(0, 10) # In this case the program don't ignore the last value(10)
player_attempts = 1
# COLORS
colors = {
    'CLEAR':'\033[m',
    'GREEN':'\033[1;32m',
    'RED':'\033[1;31m'
    }
# INPUT
print('{}MACHINE{}: Thinking in a number from 0 to 10...'.format(colors['RED'], colors['CLEAR']))
print('{}MACHINE{}: Guess the number choose by me'.format(colors['RED'], colors['CLEAR']))
player_num = int(input('{}YOU{}: '.format(colors['GREEN'], colors['CLEAR'])))
# OUTPUT
while player_num != machine_num:
    if player_num > 10:
        print('{}MACHINE{}: Wrong, I say between 0 and 10!'.format(colors['RED'], colors['CLEAR']))
    elif player_num > machine_num:
        print('{}MACHINE{}: Wrong, try lower...'.format(colors['RED'], colors['CLEAR']))
    elif player_num < machine_num:
        print('{}MACHINE{}: Wrong, try higher...'.format(colors['RED'], colors['CLEAR']))
    # new input
    player_num = int(input('{}YOU{}: '.format(colors['GREEN'], colors['CLEAR'])))
    player_attempts += 1
if player_attempts == 1:
    print('{}MACHINE{}: Wow,you got right on the first try!'.format(colors['RED'], colors['CLEAR']))
else:
    print('{}MACHINE{}: After {} attempts you got the right number!'.format(colors['RED'], colors['CLEAR'], player_attempts))