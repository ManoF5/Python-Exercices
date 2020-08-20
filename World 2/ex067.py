# COLORS
RESET = '\033[m'
RED   = '\033[31m'
GREEN = '\033[32m'
# INTRO
print('='*22)
print(f'{GREEN} Multiplication Table {RESET}')
print('='*22)
# INPUT
number = int(input(' Type a number: '))
while True:
    if number <= 0:
        print(' Bye bye...')
        break
    # OUTPUT
    print('='*70)
    for tab in range(1, 11):
        print(f' {number}\t \tx\t \t{tab}\t \t=\t \t{number * tab}')
    print('='*70)
    number = int(input(' Type another number: '))
