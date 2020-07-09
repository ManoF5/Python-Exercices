# Write a program that read two integer number and tell which is the biggest

# INPUT
n1 = int(input('Type a number: '))
n2 = int(input('Type another number: '))
# OUTPUT
if n1 > n2:
    print('\n{} > {} \n'.format(n1, n2))
else:
    print('\n{} > {} \n'.format(n2, n1))