# COLORS
colors = {
    'CLEAR':'\033[m',
    'GREEN':'\033[32m'
    }
# INPUT
distance = float(input('Type the travel distance({}Km{}): '.format(colors['GREEN'], colors['CLEAR'])))
# OUTPUT
if distance < 200:
    price = distance * 0.50
    print('\nThe price for the trip: ${} \n'.format(price))
else:
    price = distance * 0.45    
    print('\nThe price for the trip: ${} \n'.format(price))
