'''
Write a program that reads a name and three grades obtained for a student during the semester.
    1- Calculate the average (arithmetic)
    2- Inform the name and your mention:
        -Approved (average >= 7)
        -Reproved (average <= 5)
        -Retake test (average between 5.1 to 6.9)  
''' 
# COLORS
colors = {
    'CLEAN':'\033[m',
    'GREEN':'\033[32m',
    'YELLOW':'\033[33m',
    'RED':'\033[31m'
} 
# INTRO
print('Avarage Calculator')
# INPUT
name = str(input('Type your name: ')).strip()
a1 = float(input('Type your first grade: '))
a2 = float(input('Type your second grade: '))
a3 = float(input('Type your third grade:  '))
# MATH
avarage = (a1 + a2 + a3) / 3
# OUTPUT
if avarage >= 7:
    print('\nCongratulations {}! with the final result of {:.2f}, you are {}approved{}. \n'
    .format(name, avarage, colors['GREEN'], colors['CLEAN']))
elif 7 > avarage >= 5:
    print('\nYou still have a chance {}. with the final result of {:.2f}, will have to do the {}retake test{}.\n'
    .format(name, avarage, colors['YELLOW'], colors['CLEAN']))
else:
    print('\nUnfortunately {}, with the final result of {:.2f}, you are {}reproved{}.\n'
    .format(name, avarage, colors['RED'], colors['CLEAN']))