# COLORS
colors = {
    'CLEAN':'\033[m',
    'RED':'\033[31m',
    'YELLOW':'\033[33m',
    'GREEN':'\033[32m'
    }
# INPUT
n1 = float(input('Type the first number: '))
n2 = float(input('Type the second number: '))
opt = 0
while opt != 7:
    print('\n        {}Options Table{}'.format(colors['GREEN'], colors['CLEAN']))
    print('='*33) 
    print('[{}1{}] Sum'.format(colors['YELLOW'], colors['CLEAN']))
    print('[{}2{}] Subtraction'.format(colors['YELLOW'], colors['CLEAN']))
    print('[{}3{}] Multiplication'.format(colors['YELLOW'], colors['CLEAN']))
    print('[{}4{}] Division'.format(colors['YELLOW'], colors['CLEAN']))
    print('[{}5{}] Which is the highest number'.format(colors['YELLOW'], colors['CLEAN']))
    print('[{}6{}] Choose new numbers'.format(colors['YELLOW'], colors['CLEAN']))
    print('[{}7{}] Exit'.format(colors['YELLOW'], colors['CLEAN']))
    print('='*33) 
    opt = int(input('\n=> '))
# OUTPUT
    if opt == 1:
        s = n1 + n2
        print('\n |{} + {} = {}|'.format(n1, n2, s))
    elif opt == 2:
        s = n1 - n2
        print('\n |{} - {} = {}|'.format(n1, n2, s))
    elif opt == 3:
        s = n1 * n2
        print('\n |{} x {} = {}|'.format(n1, n2, s))
    elif opt == 4:
        s = n1 / n2
        print('\n |{} / {} = {}|'.format(n1, n2, s))
    elif opt == 5:
        if n1 > n2:
            print('\n |{} > {} = {}|'.format(n1, n2, s))
        else:
            print('\n |{} < {} = {}|'.format(n1, n2, s))
    elif opt == 6:
        n1 = float(input('Type the first number: '))
        n2 = float(input('Type the second number: '))
    elif opt == 7:
        print('\nGoodbye')
    else:
        print('{}\nINVALID OPTION{}'.format(colors['RED'], colors['CLEAN']))
print('\nend')