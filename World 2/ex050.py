# sum only odd numbers
total = 0
for i in range(0, 6):
    num = int(input('Type the {}º number: '.format(i+1)))
    if num % 2 == 0:
        total += num
# OUTPUT
print('\nResult: {} \n'.format(total))        