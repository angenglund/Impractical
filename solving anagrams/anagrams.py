# Load digital dictionary file as a list of words
# Accept a word from user
# Create an empty list to hold anagrams
# Sort the user-word
# Loop through each word in the word list:
#     Sort the word
#     if word sorted is equal to user-word sorted:
#         Append word to anagrams list
# Print anagrams list

import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')

anagram_list = []

# input a SINGLE word or SINGLE name below to find its anagram(s):load_dictonary
name = 'forest'
print("Input name = {}".format(name))
name = name.lower()
print("Using name = {}".format(name))

# sort name & find anagrams
name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)

# print out list of anagrams
print()
if len(anagram_list) == 0:
    print("You need a larger dictionary or a new name!")
else:
    print("Anagrams =", *anagram_list, sep='\n')
