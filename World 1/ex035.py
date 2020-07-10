# COLOR
colors = {
    'clean':'\033[m',
    'red':'\033[1;31m'
}
# INTRO
print('=' * 21)
print('{}  Triangle Analyzer {}'.format(colors['red'], colors['clean']))
print('=' * 21)
# INPUT
r1 = float(input('Enter the length of the first straight: '))
r2 = float(input('Enter the length of the second straight: '))
r3 = float(input('Enter the length of the third straight: '))
# OUTPUT
if r1 < r2 + r3 and r2 < r1  + r3 and r3 < r1 + r2:
    print('\nWith these lines it is possible to form a triangle \n')
else:
    print("\nwith these lines it ins't possible to form a triangle \n")