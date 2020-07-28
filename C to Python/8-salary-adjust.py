'''
A company that decides to adjust the employees salary according to the following criteria.   
a) 50% for the employee that earn less than three minimum wages
b) 20% for the employee that between three and ten minimum wages
c) 15% for the employee that between ten and twenty minimum wages
d) 10% for other employees
   Calculate the new salary. Write the name of the employee, the adjustment and your new salary.
'''
# DATA
minimum_wages = 1045
# INPUT
name = str(input('Type your name: '))
salary = float(input('Type your salary: $'))
# OUTPUT
if salary < (minimum_wages * 3):
    new_salary = salary * 1.5 
    print('\nName: {} \nSalary without adjustment: ${} \nAdjustment:50% \nSalary with adjustment: ${:.2f}'
    .format(name, salary, new_salary)
    )
elif (minimum_wages * 3) < salary < (minimum_wages * 10):
    new_salary = salary * 1.2
    print('\nName: {} \nSalary without adjustment: ${} \nAdjustment:20% \nSalary with adjustment: ${:.2f}'
    .format(name, salary, new_salary)
    )
elif (minimum_wages * 10) < salary < (minimum_wages *20):
    new_salary = salary * 1.15
    print('\nName: {} \nSalary without adjustment: ${} \nAdjustment:15% \nSalary with adjustment: ${:.2f}'
    .format(name, salary, new_salary)
    )
else:
    new_salary = salary * 1.1
    print('\nName: {} \nSalary without adjustment: ${} \nAdjustment:10% \nSalary with adjustment: ${:.2f}'
    .format(name, salary, new_salary)
    )