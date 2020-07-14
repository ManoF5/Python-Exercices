from datetime import date
# DATA
actual = date.today().year
# COLORS
colors = {
    'CLEAN':'\033[m',
    'GREEN':'\033[32m'
    }
# INTRO
print('---------------------')
print('{} Military Enlistment {}'.format(colors['GREEN'], colors['CLEAN']))
print('---------------------')
# INPUT
birth = int(input('Type your birthday year: '))
age = actual - birth
# OUTPUT
if age > 18:
    dif = age - 18
    if dif == 19:
        print('\nYour enlistment time passed 1 year \n')
    else:
        print('\nYour enlistment time passed {} years \n'.format(dif))
elif age == 18:
    print('\nIs time to enlist! \n')
else:
    dif = 18 - age
    if dif == 17:
        print('1 year left for your enlistment time \n')
    else:
        print('{} year left for your enlistment time \n'.format(dif))
