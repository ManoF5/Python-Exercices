# INPUT
phrase = str((input('Type a phrase: ')).upper()).strip()
# OUTPUT
print('Times the letter "A" appears:    \t \t{}'.format(phrase.count('A')) )
print('Position of the first letter "A":\t \t{}'.format(phrase.find('A') + 1) )
print('Position of the last letter "A": \t \t{}'.format(phrase.rfind('A') + 1) )
