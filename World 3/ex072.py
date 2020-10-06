# COLORS
RESET  = '\033[m'
GREEN = '\033[32m'
YELLOW  = '\033[33m'
# INTRO
print('=' * 19)
print(f'{GREEN} Extensive Numbers {RESET}')
print('=' * 19)
# DATA
extensive_number = (
    'Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten',
    'Eleven','Twelve','Thirteen','Fourteen','Fiveteen','Sixteen','Seventeen','Nineteen','Twenty'
)
# INPUT

while True:
    number = int(input(f'Type a number between {YELLOW}0{RESET} and {YELLOW}20{RESET}: '))
    if number >= 0 and number <= 20:
        break
    print('Invalid Number!try again... \n')
print(f'\nNumber in full: {YELLOW}{extensive_number[number]}{RESET}')