# Numbers: Integers and Floats
# Strings: ordered sequence of characters in quotes. Not mutable. Indexing and slicing can be performed on strings. Indexing cannot change the original string.
# Cannot modify a string, once created.
# Lists: ordered sequence of objects. group of related elements. inside square bracket, separated by comma.  Mutable. [1,2,4,'a']. Indexing and slicing can be performed
# on lists.
# Tuples: ordered sequence of objects. inside parantheses. separated by comma. (1, 2, 3, 4). Immutable.
# # Tuples are immutable
# # can perform indexing and slicing
# # index() and count()

# Dictionary: key:value pairs, unordered, mutable, cannot be sorted
# index and slicing
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("NUMBERS:")
a = (102.5/2)+(10*5)-(1**1)
print(a)

# 44
# 29
# 34
# float
sqroot = 9 ** 0.5
print(sqroot)
sq = 9 ** 2
print(sq)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

print("STRINGS:")
s = 'hello'
print(s[1])
# Reverse
print(s[::-1])
print(s[-1])
print(s[4])
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

print("LISTS:")
list_1 = []
list_1.append(0)
list_1.append(0)
list_1.append(0)
print(list_1)

# Method 2 ???
print("method2")
print([0] * 3)

list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

list4 = [5, 3, 4, 6, 1]
list4.sort()
print(list4)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

list4 = [5,4,8,9]
list4sorted = sorted(list4)
print(list4sorted)

print("DICTIONARIES:")
d = {'simple_key': 'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key': ['this is deep', ['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

print(d['k1'][2]['k2'][1]['tough'][2][0])


# Cannot sort a dictionary, since it is not a sequence.

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("TUPLES:")
# Tuples are immutable, whereas a list is mutable.

tup = (1, 2, 3, 2)
print(tup)

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("SETS:")
#  unordered, unique elements, no duplicates
list5 = [1,2,2,33,4,4,11,22,3,3,2]
set5 = set(list5)
print(set5)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

print("BOOLEAN:")
# False
# False
# False
# 3.0 == 3 --- True
# False

# "Bye" == "bye" --- False

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']

# 3>=4
# False



