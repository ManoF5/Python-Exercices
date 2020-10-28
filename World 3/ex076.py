# COLORS
RESET  = '\033[m'
GREEN = '\033[32m'
# INTRO
print('=' * 41)
print(f'{GREEN} List of Prices {RESET}')
print('=' * 41)
# INPUT
list_products_and_prices = (
    'Rice',20.0,
    'Bean',5.0,
    'Water',2.0,
    'Bread',10.0,
    'Pizza',18.0,
    'Chocolate',4.0,
    'Cake of Brigadeiro',30.0,
    'Sake',50.0,
)
# OUTPUT
for item in range(0, len(list_products_and_prices)):
    if item % 2 == 0:
        print(f' {list_products_and_prices[item]:.<30}',end='')
    else:
        print(f'R${list_products_and_prices[item]:>7}')
print('='* 41)   