# INPUT
year = int(input('Enter a year to find out if he is a bissextile: '))
# OUTPUT
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('\n{} is a bissextile year \n'.format(year))
else:
    print("\n{} isn't a bissextile year \n".format(year))