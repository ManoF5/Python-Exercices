# COLORS
RESET  = '\033[m'
GREEN = '\033[32m'
YELLOW  = '\033[33m'
# LIBRARY 
from random import randint
# DATA
while True:
    sort_numbers = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
    hi_num = -1
    low_num = 11
    # INPUT
    print('\nSort Numbers:', end=' ')
    for num in sort_numbers:
        print(f'{YELLOW}{num}{RESET}', end=' ')
        if num > hi_num:
            hi_num = num
        if num < low_num:
            low_num = num
    print('\n')
    print(f'Higher Number: {GREEN}{hi_num}{RESET}')
    print(f' Lower Number: {GREEN}{low_num}{RESET} \n')
    print('=' * 30)
    while True:
        again = str(input('Want to random again(y/n)? '))
        if again == 'y' or again == 'n':
            break
        print('Invalid answer!try again... \n')
    print('=' * 30)
    if again == 'n':
        break

print('ß®æĸ')