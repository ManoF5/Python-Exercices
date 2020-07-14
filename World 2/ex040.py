# COLORS
colors = {
    'CLEAN':'\033[m',
    'GREEN':'\033[32m',
    'YELLOW':'\033[33m',
    'RED':'\033[31m'
    }
# INTRO
print('{} ------------------ {}'.format(colors['RED'], colors['CLEAN']))
print('{}  Media Calculator  {}'.format(colors['GREEN'], colors['CLEAN']))
print('{} ------------------ {}'.format(colors['RED'], colors['CLEAN']))
# INPUT
grade1 = float(input('Type your {}first{} grade: '.format(colors['GREEN'], colors['CLEAN'])))
grade2 = float(input('Type your {}second{} grade: '.format(colors['GREEN'], colors['CLEAN'])))
# MATH
final = (grade1 + grade2) / 2
# OUTPUT
if final >= 7:
    print('\n{} APPROVED {}\n'.format(colors['GREEN'], colors['CLEAN'])) 
elif 7 > final and final >= 5:
    print('\n{} NEED TO DO THE RETAKE TEST {}\n'.format(colors['YELLOW'], colors['CLEAN']))
else:
    print('\n{} REPROVED {}\n'.format(colors['RED'], colors['CLEAN']))
