# Odd numbers and multiples of 3 from 0 to 500
num = 0
for i in range(3 , 501, 3):
    if i % 2 != 0:
        num += i
        print('0 +',i, end='')
print(' = {}'.format(num))
