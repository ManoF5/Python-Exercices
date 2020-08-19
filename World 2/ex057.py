# Continue the program until it has a valid value
sex = str(input('Type your sex(M/F): ')).upper() [0]
while sex != 'M' and sex != 'F':
    print('\033[31mInvalid Value \033[m')
    sex = str(input('Type your sex(M/F): ')).upper() [0]
print('\033[32mSuccessfully registered your sex({}) \033[m'.format(sex))   