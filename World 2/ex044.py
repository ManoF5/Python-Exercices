# COLORS
colors = {
    'CLEAN':'\033[m',
    'GREEN':'\033[32m',
    'RED':'\033[31m'
}
# INTRO
print('--------------------')
print('{} Payment Conditions {}'.format(colors['GREEN'], colors['CLEAN']))
print('--------------------')
print('{}[1]{} In cash/Bank Check - 10% off \n'.format(colors['GREEN'], colors['CLEAN']))
print('{}[2]{} Credit Card - 5% off \n'.format(colors['GREEN'], colors['CLEAN']))
print('{}[3]{} Up to 2x in Credit Card - Normal price \n'.format(colors['GREEN'], colors['CLEAN']))
print('{}[4]{} 3x or more in Credit Card - 20% interest \n'.format(colors['GREEN'], colors['CLEAN']))
# INPUT
price = float(input('Type the item price: {}${}'.format(colors['GREEN'], colors['CLEAN'])))
condition = int(input('Choose your payment condition: '))
# OUTPUT
if condition == 1:
    final = price - (price * 0.10)
    print('\nFinal price: {}${}{:.2f} \n'.format(colors['GREEN'], colors['CLEAN'], final))
elif condition == 2:
    final = price - (price * 0.05)
    print('\nFinal price: {}${}{:.2f} \n'.format(colors['GREEN'], colors['CLEAN'], final))
elif condition == 3:
    print('\nFinal price: {}${}{:.2f} \n'.format(colors['GREEN'], colors['CLEAN'], price))
elif condition == 4:
    final = price * 1.20
    print('\nFinal price: {}${}{:.2f} \n'.format(colors['GREEN'], colors['CLEAN'], final))
else:
    print('\n{}INVALID CONDITION{} \n'.format(colors['RED'], colors['CLEAN']))
