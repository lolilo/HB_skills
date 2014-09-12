

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list): # O(n)
    curr_largest = some_list[0]

    len_list = len(some_list)
    for i in xrange(1, len_list): # already looked at the first element
        if some_list[i] > curr_largest:
            curr_largest = some_list[i]

    return curr_largest

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    # inquire -- integers? decimals? 
    new = []
    for num in some_list:
        half = num / 2.0
        new.append(half)
    return new

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    length_list = []
    for i in word_list:
        length_list.append(len(i))
    return length_list

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    final = ''
    for word in string_list:
        final += word
    return final

    # remember that list.append() and list.extend() modify the original list and do not return any anything

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    sum_total = 0

    for num in numbers:
        sum_total += num # or we could use the function we wrote earlier

    average = float(sum_total)/len(numbers)
    return average

l = range(-10, 10)
l2 = [6, 7]
words = ['yo', 'i', 'make', 'words']

print largest(l)
print halvesies(l)
print word_lengths(words)
print sum_numbers(l)
print mult_numbers(l2)
print join_strings(words) == ''.join(words)
print average(l2) == float(sum(l2)) / len(l2)