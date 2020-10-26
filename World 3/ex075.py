# COLORS
RESET  = '\033[m'
RED = '\033[31m'
GREEN = '\033[32m'
# DATA
even = False
# INTRO
print('=' * 26)
print(f' {GREEN}Data analysis in a Tuple {RESET}')
print('=' * 26)
# INPUT
num = (int(input('Type the first number: ')),
    int(input('Type the second number: ')),
    int(input('Type the third number: ')),
    int(input('Type the fourth number: ')))
print("You type the values:",num,'\n')
# A
print(f"A: The number 9 appeared {GREEN}{num.count(9)}{RESET} times")
# B
print(f"B: The first appearance of number 3 was in the {GREEN}{num.index(3)+1}{RESET}º position")
# C
print(f'C: The even number entered:',end=' ')
for n in num:
    if n % 2 == 0:
        print(f'{GREEN}{n}{RESET}',end=' ')
        even = True
    if even == False:
        print(f'{RED}Not Found{RESET}')
print('\n')