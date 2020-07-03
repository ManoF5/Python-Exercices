# INPUT
distance = float(input('Type the travel distance(Km): '))
# OUTPUT
if distance < 200:
    price = distance * 0.50
    print('\nThe price for the trip: ${} \n'.format(price))
else:
    price = distance * 0.45    
    print('\nThe price for the trip: ${} \n'.format(price))
