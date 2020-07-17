# COLORS
colors = {
    'CLEAN':'\033[m',
    'GRAY':'\033[37m',
    'GREEN':'\033[32m',
    'YELLOW':'\033[33m',
    'RED':'\033[31m'
}
# INTRO
print('-----------------')
print('{} Body Mass index {}'.format(colors['GREEN'], colors['CLEAN']))
print('-----------------')
# INPUT
height = float(input('Type your height: '))
weight = float(input('Type your weight: '))
# MATH
bmi = weight / height**2
# OUTPUT
if 18.5 > bmi:
    print('\n{} Underweight {}\n'.format(colors['GRAY'], colors['CLEAN']))
elif 18.5 < bmi and bmi < 25:
    print('\n{} Normal(healthy weight) {}\n'.format(colors['GREEN'], colors['CLEAN']))
elif 25 < bmi and bmi < 30:
    print('\n{} Overweight {}\n'.format(colors['GRAY'], colors['CLEAN'])) 
elif 30 < bmi and bmi < 30:
    print('\n{} Obese {}\n'.format(colors['YELLOW'], colors['CLEAN'])) 
else:  
    print('\n{} Severely Obese {}\n'.format(colors['RED'], colors['CLEAN'])) 