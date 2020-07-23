# DATA
minority = 0
adulthood = 0
# INPUT
for i in range(0, 6):
    age = int(input('Type your birth year: '))
    if age < 18: 
        minority += 1
    else:
        adulthood += 1
# OUTPUT
print('\nPeople\n Minority: {} \n Adulthood: {} \n'.format(minority, adulthood))
