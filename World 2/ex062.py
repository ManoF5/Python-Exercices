# COLORS
colors = {
    'CLEAN':'\033[m',
    'GREEN':'\033[32m'
}
# INTRO
print('='*24)
print('{} Arithmetic Progression {}'.format(colors['GREEN'], colors['CLEAN']))
print('='*24)
# INPUT
first_term = int(input(' Type the first term: '))
common_dif = int(input(' Type the common difference: '))
term = first_term
# OUTPUT
# Part 1
print('='*32)
i = 0
while i < 10:
    print(' {}{}º{} term:\t \t{}'.format(colors['GREEN'], i+1,colors['CLEAN'] , term))
    term += common_dif
    i += 1
print('='*32)
# Part 2
opt = 1
position = 11
print('You want see more numbers?')
while opt != 0:
    opt = int(input('Type how many you want to see or type 0 to leave: '))
    i = 0
    print('='*32)
    while i < opt:
        print(' {}{}º{} term:\t \t{}'.format(colors['GREEN'], position ,colors['CLEAN'] , term))
        term += common_dif
        position += 1
        i += 1
    print('='*32)
print('\n Goodbye')