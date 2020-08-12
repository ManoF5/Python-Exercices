# COLORS
colors = {
    'CLEAN':'\033[m',
    'RED':'\033[31m'
}
# INTRO
print('=' * 20)
print('{} Fibonacci Sequence {}'.format(colors['RED'], colors['CLEAN']))
print('=' * 20)
# INPUT
num = int(input('How many terms you want to show: '))
# OUTPUT
f1 = 0
f2 = 1
count = 3
print('\n{}{}{} -> {}{}{} ->'.format(colors['RED'], f1, colors['CLEAN'], colors['RED'], f2, colors['CLEAN']), end='')
while count <= num:
    f3 = f1 + f2
    print(' {}{}{} ->'.format(colors['RED'], f3, colors['CLEAN']), end='')
    f1 = f2
    f2 = f3
    count += 1
print(' end \n')