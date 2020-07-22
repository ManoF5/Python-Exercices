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
print('='*31)
for i in range(0,10):
    print(' {}{}º{} term:\t \t{}'.format(colors['GREEN'], i+1,colors['CLEAN'] , term))
    term += common_dif
print('='*31)