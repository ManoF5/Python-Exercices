# COLORS
colors = {
    'CLEAN':'\033[m',
    'GREEN':'\033[32m'
}
# DATA
hi_weight = 0
low_weight = 1000
# INTRO
print('='*27)
print('{} Highest and Lowest Weight {}'.format(colors['GREEN'], colors['CLEAN']))
print('='*27)
# INPUT
for i in range(0,5):
    weight = float(input('Type your weight: ')) 
    if weight > hi_weight:
        hi_weight = weight
    if weight < low_weight:
        low_weight = weight
# OUTPUT
print('\n{}highest{} weight: {}'.format(colors['GREEN'], colors['CLEAN'], hi_weight))
print('{}Lowest{} weight: {} \n'.format(colors['GREEN'], colors['CLEAN'], low_weight))