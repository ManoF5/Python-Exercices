# INPUT
n1 = int(input('Type a number: '))
n2 = int(input('Type another number: '))
# OUTPUT
if n1 > n2:
    print('\nThe first number is higher \n{} > {} \n'.format(n1, n2))
elif n2 > n1:
    print('\nThe second number is higher \n{} > {} \n'.format(n2, n1))
else:
    print('\nThe two number is equal \n{} = {} \n'.format(n1, n2))
