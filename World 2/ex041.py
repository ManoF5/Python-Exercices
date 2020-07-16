from datetime import date
# DATA
actual = date.today().year
# COLORS
colors = {
    'CLEAN':'\033[m',
    'GRAY':'\033[37m',
    'YELLOW':'\033[33m',
    'GREEN':'\033[32m',
    'CYAN':'\033[36m',
    'BLUE':'\033[34m'
    }
# INTRO
print('-----------------------------')
print('{} Swimming Age Classification {}'.format(colors['BLUE'], colors['CLEAN']))
print('-----------------------------')
print('{} MIRIN {} \n 0-9 years \n'.format(colors['GRAY'], colors['CLEAN']))
print('\n{} CHILD {} \n 9-14 years \n'.format(colors['YELLOW'], colors['CLEAN']))
print('\n{} JUNIOR {} \n 14-19 years \n'.format(colors['GREEN'], colors['CLEAN']))
print('\n{} SENIOR {} \n 19-20 years \n'.format(colors['CYAN'], colors['CLEAN']))
print('\n{} MASTER {} \n above 2O years\n'.format(colors['BLUE'], colors['CLEAN']))
# INPUT
birth = int(input('Type your birthday year: '))
# MATH
age = actual - birth
# OUTPUT
if 9 > age:
    print('\n{} MIRIM {}\n'.format(colors['GRAY'], colors['CLEAN']))
elif 9 < age and age < 14:
    print('\n{} CHILD {}\n'.format(colors['YELLOW'], colors['CLEAN']))
elif 14 < age and age < 19:
    print('\n{} JUNIOR {}\n'.format(colors['GREEN'], colors['CLEAN']))
elif 19 < age and age < 20:
    print('\n{} SENIOR {}\n'.format(colors['CYAN'], colors['CLEAN']))
else:
    print('\n{} MASTER {}\n'.format(colors['BLUE'], colors['CLEAN']))