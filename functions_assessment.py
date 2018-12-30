# Problem:1
# def vol(rad):
#     volume = (4/3) * 3.14 * (rad ** 3)
#     return volume
#
# print(vol(2))


# # Problem:2
#
# def ran_check(num,low,high):
#     #     return num <= high and num >= low
#       return num in range(low,high+1)
#
# print(ran_check(12,4,12))


#Problem:3
# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33


# #
# def letter_case(st):
#     upper_count = 0
#     lower_count = 0
#     for letter in st:
#         if letter == letter.upper():
#             upper_count = upper_count + 1
#         elif letter == letter.lower():
#             lower_count = lower_count + 1
#         else:
#             pass
#
#     return upper_count, lower_count
# print(letter_case('ThisinnnguiKIYioLLL MKInhn'))
# # # .isupper()
# # .islower()
#


# Problem 4:
# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# # Unique List : [1, 2, 3, 4, 5]

# #
# def list_a(a):
#     unique_list_a = list(set(a))
#     return unique_list_a
#
# print(list_a([1,2,1,3,1,5,5,4]))

#
#
#
#
# l = [1,2,3,3]
# s = set(l)
# print(s)
#
#
# # Problem 5:
# Write a Python function to multiply all the numbers in a list.
# Sample List : [1, 2, 3, -4]
# Expected Output : -24
#
#
# def list_multiply(x):
#     multiply = 1
#     for n in x:
#         multiply *= n
#     return multiply
#
# print(list_multiply([1,2,4,5,-8]))


#
# # Problem 6:
# Write a Python function that checks whether a passed in string is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
# #
# def is_palindrome(s):
#     list_st = list(s)
#     reverse_st = list_st[::-1]
#     if reverse_st == list(s):
#         return True
#     else:
#         return False
#
# print(is_palindrome("helleh"))
# #
# #
# #


def palindrome(s):
    return s == s[::-1]
print(palindrome('heloleh'))


