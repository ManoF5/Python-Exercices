# COLORS
colors = {
    'CLEAN':'\033[m',
    'GREEN':'\033[32m',
    'RED':'\033[31m'
}
# INTRO
print('=' * 21)
print('{}  Triangle Analyzer {}'.format(colors['GREEN'], colors['CLEAN']))
print('=' * 21)
# INPUT
r1 = float(input('Enter the length of the {}first{} straight: '.format(colors['GREEN'], colors['CLEAN'])))
r2 = float(input('Enter the length of the {}second{} straight: '.format(colors['GREEN'], colors['CLEAN'])))
r3 = float(input('Enter the length of the {}third{} straight: '.format(colors['GREEN'], colors['CLEAN'])))
# OUTPUT
if r1 < r2 + r3 and r2 < r1  + r3 and r3 < r1 + r2:
    print('\nWith these lines it {}is possible{} to form a triangle'.format(colors['GREEN'], colors['CLEAN']))
    if r1 == r2 and r1 == r3:
        print('Type: {}Equilateral Triangle{} \n'.format(colors['GREEN'], colors['CLEAN']))
    elif (r1 == r2 and r1 != r3) or (r1 == r3 and r1 != r2) or (r2 == r3 and r2 != r1):
        print('Type: {}Isosceles Triangle{} \n'.format(colors['GREEN'], colors['CLEAN']))
    else:
        print('Type: {}Scalene Triangle{} \n'.format(colors['GREEN'], colors['CLEAN']))
else:
    print("\nWith these lines it {}ins't possible{} to form a triangle \n".format(colors['RED'], colors['CLEAN']))