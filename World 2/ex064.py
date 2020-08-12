# COLORS
colors = {
    'CLEAN':'\033[m',
    'GREEN':'\033[32m'
}
# INPUT
num = 0
total = 0
while num != 999:
    num = int(input('Type a number,if you want to stop, type 999:{} '.format(colors['GREEN'])))
    print(colors['CLEAN'])
    if num != 999:
        total += num
# OUTPUT
print('Total Sum: {}{}{}'.format(colors['GREEN'], total, colors['CLEAN']))