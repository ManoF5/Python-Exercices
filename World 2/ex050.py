# sum only odd numbers
total = 0
count = 0
for i in range(0, 6):
    num = int(input('Type the {}º number: '.format(i+1)))
    if num % 2 == 0:
        total += num
        count += 1
# OUTPUT
if count != 1:
    print('\nYou type {} odd numbers and the sum is equal to {}\n'.format(count, total)) 
else:
    print('\nYou type only one odd number, so there is no sum\n')      