# COLORS
RESET = '\033[m'
RED   = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
# DATA
i = 1
adulthood = man_quant = woman_below_20 = 0
# INPUT 
while True:
    # AGE
    print('='* 44)
    age = int(input(f'Type the age for the {GREEN}{i}º{RESET} person: '))
    if age > 18:
        adulthood += 1
    # SEX
    sex = str(input(f'Type the sex for the {GREEN}{i}º{RESET} person(m/f): ')).upper() [0]
    while sex != 'M' and sex != 'F':
        sex = str(input(f'{RED}Wrong answer!{RESET}\nType the sex for the {GREEN}{i}º{RESET} person(m/f): ')).upper() [0]
    if sex == 'M':
        man_quant += 1
    if sex == 'F' and age < 20:
        woman_below_20 += 1
    print('='* 44)
    # AGAIN?
    again = str(input(f'You want to register a new person?({GREEN}y{RESET}/{RED}n{RESET}): ')).upper() [0]
    while again != 'Y' and again != 'N':
        again = str(input(f'{RED}Wrong answer!{RESET} try again\nYou want to register a new person?(y/n): ')).upper() [0]
    if again == 'Y':
        i += 1
    elif again == 'N':
        break
# OUTPUT   
print('=' * 34)
print(f'People in adulthood: {GREEN}{adulthood}{RESET}')
print(f'Registered men: {GREEN}{man_quant}{RESET}')
print(f'Woman under 20: {GREEN}{woman_below_20}{RESET}')
print('=' * 34)
