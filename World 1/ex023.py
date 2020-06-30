# INPUT
num = int(input('Type a number(0-9999): '))
# MATH
u = num // 1 % 10
t = num // 10 % 10
h = num // 100 % 10
th = num // 1000 % 10
# OUTPUT
print("analyzing... \n")
print('Unity:    \t \t{}'.format(u))
print('Ten:      \t \t{}'.format(t))
print('Hundred:  \t \t{}'.format(h))
print('Thousands:\t \t{} \n'.format(th))
