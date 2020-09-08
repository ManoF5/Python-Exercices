# COLORS
RESET  = '\033[m'
RED    = '\033[31m'
GREEN  = '\033[32m'
YELLOW = '\033[33m'
# INTRO
print('=' * 14)
print(f'{GREEN} Product List {RESET}')
print('=' * 14)
# DATA
i = 1
total_price = above_1000 = 0
# INPUT
while True:
    print(f'{i}º Product')
    product_name = str(input('Type the product name: ')).strip()
    product_price = float(input(f'Type the product price: {GREEN}${RESET}'))
    print('=' * 41)
    # QUESTION A
    total_price += product_price
    # QUESTION B
    if product_price > 1000:
        above_1000 += 0
    # QUESTION C
    if i == 1:
        cheaper = product_price
        cheaper_item_name = product_name
    else:
        if product_price < cheaper:
            cheaper = product_price
            cheaper_item_name = product_name
    # REPETITION SYSTEM
    again = str(input(f'You want to register a new product?({YELLOW}y/n{RESET})\nR: ')).upper() [0]
    while again != 'Y' and again != 'N':
        again = str(input(f'{RED}Wrong answer!{RESET} try again\nYou want to register a new Product?({YELLOW}y/n{RESET})\nR: ')).upper() [0]
    if again == 'Y':
        i += 1
        print('=' * 41)
    elif again == 'N':
        break
# OUTPUT
print('=' * 31)
print(f'Final price: {GREEN}${RESET}{total_price}')
print(f'How many items above {GREEN}${RESET}1000: {above_1000}')
print(f'The cheapest item: {cheaper_item_name}')
print('=' * 31)