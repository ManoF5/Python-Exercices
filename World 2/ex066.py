# COLORS
RESET = '\033[m'
RED   = '\033[31m'
GREEN = '\033[32m'
# INPUT
total_num = total_sum = 0
while True:
    num = int(input(f'Type a number({RED}999 to stop{RESET}): ') )
    if num == 999:
        break
    total_num += 1
    total_sum += num
# OUTPUT
print(f'\nTotal of numbers: {GREEN}{total_num}{RESET}')
print(f'Total Sum: {GREEN}{total_sum}{RESET}')