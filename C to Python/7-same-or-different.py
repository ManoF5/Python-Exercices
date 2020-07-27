'''
Do a program that read two numbers and identify if they are the same or different. 
if they are the same, insert a message saying that they are the same. 
else, tell which ones the highest number.
'''
# INPUT
n1 = int(input('Type the first number: '))
n2 = int(input('Type the second number: '))
# OUTPUT
if n1 == n2:
    print('\nYour type the same number\n')
elif n1 > n2:
    print('\nThe first number is higher than the second\n'
    '======= \n'
    ' {} > {} \n'
    '======= \n'
    .format(n1, n2))
else:
    print('\nThe second number is greater than the first\n'
    '======= \n'
    ' {} > {} \n'
    '======= \n'
    .format(n2, n1))