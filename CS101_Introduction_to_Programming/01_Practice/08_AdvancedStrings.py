# --------------------------------------
# Write a function called check_for_name that takes two strings as parameters named sentence and name. 
# The function should return True if name appears in sentence in all lowercase letters, all uppercase letters, or with any mix of uppercase and lowercase letters. 
# The function should return False otherwise.

def check_for_name(sentence, name):
  return name.lower() in sentence.lower()
# Uncomment these function calls to test your  function:
#print(check_for_name("My name is Jamie", "Jamie"))
# should print True
#print(check_for_name("My name is jamie", "Jamie"))
# should print True
#print(check_for_name("My name is Samantha", "Jamie"))
# should print False

# --------------------------------------
# Write a function named count_char_x that takes a string named word and a single character named x as parameters. The function should return the number of times x appears in word.

def count_char_x(word, x):
  count = 0
  for letter in word:
    if (x == letter):
      count += 1
  return count
# Uncomment these function calls to test your function:
#print(every_other_letter("Codecademy"))
# should print Cdcdm
#print(every_other_letter("Hello world!"))
# should print Hlowrd
#print(every_other_letter(""))
# should print 

# --------------------------------------
# Write a function named reverse_string that has a string named word as a parameter. The function should return word in reverse.

def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse
# Uncomment these function calls to test your function:
#print(reverse_string("Codecademy"))
# should print ymedacedoC
#print(reverse_string("Hello world!"))
# should print !dlrow olleH
#print(reverse_string(""))
# should print

# --------------------------------------
# Write a function called make_spoonerism that takes two strings as parameters named word1 and word2. Finding the first syllable of a word is a difficult task, so for our function, we’re going to switch the first letters of each word. Return the two new words as a single string separated by a space.

def make_spoonerism(word1, word2):
  return word2[0]+word1[1:]+" "+word1[0]+word2[1:]
# Uncomment these function calls to test your function:
#print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
#print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
#print(make_spoonerism("a", "b"))
# should print b a

# --------------------------------------
# Create a function named add_exclamation that has one parameter named word. This function should add exclamation points to the end of word until word is 20 characters long. If word is already at least 20 characters long, just return word.

def add_exclamation(word):
  while(len(word) < 20):
    word += "!"
  return word
# Uncomment these function calls to test your function:
#print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
#print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn