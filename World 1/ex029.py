max_velocity = 80
# INPUT
velocity = float(input('Type the velocity of the car(km): '))
# OUTPUT
print('Allowed speed: {}km'.format(max_velocity))
if velocity > max_velocity:
    print('\nYou have exceeded the speed limit!')
    fine = (velocity - max_velocity) * 7
    print('Fine => every km exceeded = $7')
    print('Traffic ticket: ${}'.format(fine))
else:
    print('\nYou are below the limit')