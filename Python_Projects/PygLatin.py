pyg = 'ay'

# Input statement 
original = input('Enter a word: ')

# If word has chars & only letters, print. If not say "empty"
if len(original) > 0 and original.isalpha():
  print(original)
else:
  print('empty')

# variable word displays original but all lower case
word = original.lower()
# print(word)

# Variable first holds first character of word
first = word[0]
# print(first)

# New variable through concatenation
new_word = word + first + pyg
#print(new_word)

# Variable new_word updated through slicing 
new_word = new_word[1:len(new_word)]
print(new_word)