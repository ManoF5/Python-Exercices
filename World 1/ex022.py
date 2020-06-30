# INPUT
name = str(input('Type your full name: ')).strip()
# OUTPUT
print('Analyzing... \n')
print('Your name capitalized:',name.upper())
print('Your name in lower case:',name.lower())
print('Your name has {} letters'.format(len(name) - name.count(' ')))
# print('Your first name have {} letters \n'.format(name.find(' ')))
split = name.split()
print('Your first name is {} and have {} letters \n'.format(split[0], len(split[0])))
