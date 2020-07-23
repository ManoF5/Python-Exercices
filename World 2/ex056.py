# COLORS
colors = {
    'CLEAN':'\033[m',
    'GREEN':'\033[32m'
}
# DATA
people_quant = 6
avarage = 0
older_male = 0
older_male_name = ''
womans_under20 = 0
# INPUT
for i in range(0,people_quant):
    name = str(input('\n{}Type your name:{} '.format(colors['CLEAN'], colors['GREEN']))).strip()
    age = int(input('{}Type your age:{} '.format(colors['CLEAN'], colors['GREEN'])))
    sex = str(input('{}Type your sex(M/F):{} '.format(colors['CLEAN'], colors['GREEN']))).strip().upper()
    avarage += age
    if age > older_male and sex == 'M':
        older_male = age
        older_male_name = name
    if age < 20 and sex == 'F':
        womans_under20 += 1
# OUTPUT
print('\nAvarage age of the group: {}{:.2f}{}'.format(colors['GREEN'], (avarage / people_quant), colors['CLEAN']))
print('Olderst man in the group: {}{}{}'.format(colors['GREEN'], older_male_name, colors['CLEAN']))
print('Amount of womans under 20 years: {}{}{}\n'.format(colors['GREEN'], womans_under20, colors['CLEAN']))