from random import randint
machine_num = randint(0, 10)
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
    print('{}MACHINE{}: Wrong, try again...'.format(colors['RED'], colors['CLEAR'])) 
    player_num = int(input('{}YOU{}: '.format(colors['GREEN'], colors['CLEAR'])))
    player_attempts += 1
if player_attempts == 1:
    print('{}MACHINE{}: Wow,you got right on the first try!'.format(colors['RED'], colors['CLEAR']))
else:
    print('{}MACHINE{}: After {} attempts you got the number right'.format(colors['RED'], colors['CLEAR'], player_attempts))