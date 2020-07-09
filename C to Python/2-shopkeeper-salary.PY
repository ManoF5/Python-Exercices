# INPUT
name = str(input('Input your name: ')).strip
fixed_salary = float(input('Fixed salary: $ '))
sales_month = float(input('Sales in the month: $'))
# MATH 
salary = fixed_salary + (sales_month * 0.15)
# OUTPUT
print('\nHello {}'.format(name))
print('Fixed salary \t \t Sales percentages \t \t total salary\n'
      '{}        \t \t {}                \t \t {} \n'.format(fixed_salary, (sales_month * 0.15), salary))
