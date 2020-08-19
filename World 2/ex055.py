# COLORS
colors = {
    'CLEAN':'\033[m',
    'GREEN':'\033[32m'
}
# DATA
hi_weight = 0
low_weight = 0
# INTRO
print('='*27)
print('{} Highest and Lowest Weight {}'.format(colors['GREEN'], colors['CLEAN']))
print('='*27)
# INPUT
for i in range(0,5):
    weight = float(input('Type the weight of the {}° person: '.format(i+1))) 
    if i == 0:
        hi_weight = weight
        low_weight = weight
    else:
        if weight > hi_weight:
            hi_weight = weight
        if weight < low_weight:
            low_weight = weight
# OUTPUT
print('\n{}highest{} weight: {}Kg'.format(colors['GREEN'], colors['CLEAN'], hi_weight))
print('{}Lowest{} weight: {}Kg \n'.format(colors['GREEN'], colors['CLEAN'], low_weight))