from datetime import date
# DATA
current_year = date.today().year
minority = 0
adulthood = 0
# INPUT
for i in range(0, 7):
    birth_year = int(input('Type the birth year of the {}° person: '.format(i+1)))
    age = current_year - birth_year
    if age < 18: 
        minority += 1
    else:
        adulthood += 1
# OUTPUT
print('\nPeople\n Minority: {} \n Adulthood: {} \n'.format(minority, adulthood))
