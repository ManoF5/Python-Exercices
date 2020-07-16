# COLORS
colors = {
    'CLEAN':'\033[m',
    'GREEN':'\033[32m',
    'RED':'\033[31m'
    }
# INTRO
print(' --------------------------- ')
print('{}  Bank Loan: House Purchase {}'.format(colors['GREEN'], colors['CLEAN']))
print(' --------------------------- ')
# INPUT
house_value = float(input('House value: {}${}'.format(colors['GREEN'], colors['CLEAN'])))
salary = float(input('Your salary: {}${}'.format(colors['GREEN'], colors['CLEAN'])))
months = int(input('Divided into how many months: '))
# MATH
quote = house_value / months
# OUTPUT
if quote < (salary * 0.30):
    print('\n{} Loan Accepted {}\n'.format(colors['GREEN'], colors['CLEAN']))
else:
    print('\n{} Loan Denied {}\n'.format(colors['RED'], colors['CLEAN']))