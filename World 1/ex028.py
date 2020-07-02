from random import choice
numbers = [0, 1, 2, 3 , 4, 5]
machine_num = choice(numbers)
# INPUT
print('Try to find the number chosen by the machine')
num = int(input('type a number(0-5): '))
# OUTPUT
if num == machine_num:
    print('\nYou wins!')
else:
    print('\nMachine wins!')
    print('Better luck next time')
