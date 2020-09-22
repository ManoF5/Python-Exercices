# COLORS
RESET  = '\033[m'
GREEN  = '\033[32m'
# DATA
money50 = 0
money20 = 0
money10 = 0
money1 = 0
# INTRO
print('=' * 13)
print(f'{GREEN} ATM Machine {RESET}')
print('=' * 13)
# INPUT
value = int(input('How much you do you want to withdraw: '))
while True:
    if value >= 50:    # $50
        money50 += 1
        value -= 50
    elif value <= 50 and value >= 20:    # $20
        money20 += 1
        value -= 20
    elif value <= 20 and value >= 10:    # $10
        money10 += 1
        value -= 10
    elif value < 10:    # $1
        money1 += 1
        value -= 1
    # exit
    if value == 0:
        break
print(
'==============\n'
f' {GREEN}${RESET}50 cash: {money50} \n'
f' {GREEN}${RESET}20 cash: {money20} \n'
f' {GREEN}${RESET}10 cash: {money10} \n'
f' {GREEN}${RESET} 1 cash: {money1}  \n'
'==============\n'
)