# COLORS
colors = {
    'CLEAN':'\033[m',
    'GREEN':'\033[32m'
}
# INTRO

# INPUT
opt = 1
total_sum = 0
count = 0
hi_num = 0
lo_num = 1000
while opt != 0:
    num = int(input('Type a number: '))
    # AVERAGE
    total_sum += num
    count += 1
    # HIGHER AND LOWER NUMBER
    if num > hi_num:
        hi_num = num
    if num < lo_num:
        lo_num = num
    opt = int(input('Want to continue?\n[1] Continue \n[0] Leave\n>>> '))
# OUTPUT
average = total_sum / count
print('Average: {:.2f} \n'
'Higher Number: {} \n'
'Lower Number: {}'.format(average, hi_num, lo_num))