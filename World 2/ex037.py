# COLORS
colors = {
    'CLEAN':'\033[m',
    'GREEN':'\033[32m'
    }
# INTRO
print('Base Converter')
# INPUT
num = int(input('\nType a decimal number: '))
print('\nType of conversions')
print('  [1] Binary')
print('  [2] Octal')
print('  [3] Hexadecimal')
tp = int(input('Choose the type: '))
# OUTPUT
if tp == 1:
    print('\n{} in binary: {} \n'.format(num, bin(num)[2:]))
elif tp == 2:
    print('\n{} in octal: {} \n'.format(num, oct(num)[2:]))
elif tp == 3:
    print('\n{} in hexadecimal: {} \n'.format(num, hex(num)[2:]))
else:
    print('\nINVALID NUMBER/TYPE \n')