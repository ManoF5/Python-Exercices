# Continue the program until it has a valid value
sex = str(input('Type your sex(M/F): ')).upper()
while sex != 'M' and sex != 'F':
    print('\033[31mInvalid Value \033[m')
    sex = str(input('Type your sex(M/F): ')).upper()
    