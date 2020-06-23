# INPUT
salary = float(input("What is the employee's salary:$"))
increase = float(input("Percentage of salary increase: "))
# MATH
final_salary = salary * ((increase / 100) + 1)
# OUTPUT
input("Salary without increase:${:.2f} \n"
      "Increase:{}% \n"
      "Salary with increase:${:.2f} \n".format(salary, increase, final_salary))
