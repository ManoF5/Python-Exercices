# COLORS
colors = {
    'CLEAN':'\033[m',
    'GREEN':'\033[32m',
    'RED':'\033[31m'
}
# INTRO
print('='*15)
print('\033[32m Prime Numbers \033[m')
print('='*15)
# INPUT
num = int(input('Type a number: '))
total = 0
print('\n')
# OUTPUT
for i in range(1, num + 1):
    if num % i == 0:
        print(colors['GREEN'], end='')
        total += 1
    else:
        print(colors['RED'], end='')
    print('{} '.format(i), end='')    
print('\n{}Divisible for {} numbers'.format(colors['CLEAN'], total))
if total == 2:
    print('Is a prime number \n')
else:
    print("Isn't a prime number \n")
