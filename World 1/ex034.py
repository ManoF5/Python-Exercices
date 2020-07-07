# INPUT
salary = float(input('Hello,please type your salary: '))
# OUTPUT
if salary <= 1250:
    new_salary = salary * 1.15
    print('With the 15% increase, the value of the new salary is ${}'.format(new_salary))
else:
    new_salary = salary * 1.10
    print('With the 10% increase, the value of the new salary is ${} \n'.format(new_salary))