# --------------------------------------
# Write a function called unique_english_letters that takes the string word as a parameter. The function should return the total number of unique letters in the string. Uppercase and lowercase letters should be counted as different letters.
# We’ve given you a list of every uppercase and lower case letter in the English alphabet. It will be helpful to include that list in your function.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques
# Uncomment these function calls to test your function:
# print(unique_english_letters("mississippi"))
# should print 4
# print(unique_english_letters("Apple"))
# should print 4

# --------------------------------------
# Write a function named count_char_x that takes a string named word and a single character named x as parameters. The function should return the number of times x appears in word.

def count_char_x(word, x):
  count = 0
  for letter in word:
    if (x == letter):
      count += 1
  return count
# Uncomment these function calls to test your tip function:
# print(count_char_x("mississippi", "s"))
# should print 4
# print(count_char_x("mississippi", "m"))
# should print 1

# --------------------------------------
# Write a function named count_multi_char_x that takes a string named word and a string named x. This function should do the same thing as the count_char_x function you just wrote - it should return the number of times x appears in word. However, this time, make sure your function works when x is multiple characters long.
# For example, count_multi_char_x("Mississippi", "iss") should return 2

def count_multi_char_x(word, x):
  splits = word.split(x)
  return(len(splits)-1)
# Uncomment these function calls to test your function:
#print(count_multi_char_x("mississippi", "iss"))
# should print 2
#print(count_multi_char_x("apple", "pp"))
# should print 1

# --------------------------------------
# Write a function named substring_between_letters that takes a string named word, a single character named start, and another character named end. This function should return the substring between the first occurrence of start and end in word. If start or end are not in word, the function should return word.
# For example, substring_between_letters("apple", "p", "e") should return "pl".

def substring_between_letters(word, start, end):
  start_ind = word.find(start)
  end_ind = word.find(end)
  if start_ind > -1 and end_ind > -1:
    return(word[start_ind+1:end_ind])
  return word
# Uncomment these function calls to test your function:
#print(substring_between_letters("apple", "p", "e"))
# should print "pl"
#print(substring_between_letters("apple", "p", "c"))
# should print "apple"

# --------------------------------------
# Create a function called x_length_words that takes a string named sentence and an integer named x as parameters. This function should return True if every word in sentence has a length greater than or equal to x.

def x_length_words(sentence, x):
  words = sentence.split(" ")
  for word in words:
    return len(word) >= x
# Uncomment these function calls to test your tip function:
# print(x_length_words("i like apples", 2))
# should print False
# print(x_length_words("he likes apples", 2))
# should print True