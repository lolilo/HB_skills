from os.path import exists

string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "San", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys and the number of each element as
the value.
Bonus: Do the same for a file (i.e. twain.txt)
"""
def count_unique(string1):
    list_of_strings = string1.split(' ')
    d = {}
    for string in list_of_strings:
        if d.get(string):
            d[string] += 1
        else: 
            d[string] = 1
    return d

# print count_unique(string1)

FILE_PATH = 'test.txt'
def count_unique_from_file(input_file):
    isValid = True

    if not exists(input_file):
        return "%r does not exist!" % input_file

    if isValid:
        in_file = open(input_file)
        in_file_ended = False # Is cursor at the end of the file? 

        def add_to_dictionary(dictionary, key):
            if dictionary.get(key):
                dictionary[key] += 1
            else:
                dictionary[key] = 1

        d = {}
        
        # could I just do in_file .split() instead of line by line?
        while not in_file_ended:
            current_line = in_file.readline()

            if current_line == '': # you have reached the end of the file
                in_file_ended = True
                in_file.close()
                break

            string_list = current_line.split()
            for string in string_list:
                add_to_dictionary(d, string)

        return d

# print count_unique_from_file(FILE_PATH)

"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):
    pass

"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
    # can we optimize this if the two lists are not the same length? Does it matter? 
    # I don't think so. Still need to iterate through both lists once.
    # No time optimization, but space optimization if you create dict with smaller list!
    # d = {}


    # What if there are duplicates in both lists? Then you would need a dictionary. 
    # Keys as list items, value as number of occurances. Fun. ^__^

    s = set()
    for item in list1:
        if item in s:
            pass
        else: 
            s.add(item)

    common = []
    for item in list2:
        if item in s:
            common.append(item)

    return common

# print common_items2(list1, list2)

"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):
    number_pairs = []
    for num in list1:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1

    for key in d.keys():
        pair = 0 - key 
        if pair in d:
            d[pair] -= 1

    return number_pairs

"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
    pass

"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
    pass

"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""


