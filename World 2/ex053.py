# COLORS
colors = {
    'CLEAN':'\033[m',
    'GREEN':'\033[32m',
    'RED':'\033[31m'
}
# INTRO
print('='*26)
print('{} Palindrome Phrase Verify {}'.format(colors['GREEN'], colors['CLEAN']))
print('='*26)
# INPUT
phrase = str(input('Type a phrase: ')).strip().upper()
words = phrase.split()
all_words = ''.join(words)
reverse = ''
for letter in range(len(all_words) - 1, -1, -1):
    reverse += all_words[letter]
# OUTPUT
if all_words == reverse:
    print('\n{}Is a palindrome{}'.format(colors['GREEN'], colors['CLEAN']))
else:
    print("\n{}Ins't a palindrome{}".format(colors['RED'], colors['CLEAN']))
print('Normal:  {} \nReverse: {} \n'.format(all_words, reverse))
