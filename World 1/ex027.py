# INPUT
name = str(input('Type your full name: ')).strip()
split_name = name.split()
# OUTPUT
print('\nIs a pleasure to meet you!')
print('Your first name is {} \nand your last is {} \n'.format(split_name[0], split_name[len(split_name)- 1]) )
