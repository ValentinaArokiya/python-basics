# LIST COMPREHENSIONS
# unique way of quickly creating lists
# Alternative to using a for loop along with .append() to create a list
# syntax: new_list = [element for element in an_iterable_item]


print("Basic syntax:")
mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)
print("________________________________________________________")


print('\n')
# syntax: new_list = [element for element in an_iterable_item]
print("List Comprehension:")
mystring1 = 'hello'
mylist = [letter for letter in mystring1]
print(mylist)

print("----------------------------------------------------------")

mylist2 = [a for a in 'world']
print(mylist2)

print("____________________________________________________________")
print("\n")

mylist3 = [num for num in range(0,11)]
print(mylist3)

print("____________________________________________________________")
print("\n")

mylist3 = [num ** 2 for num in range(0,11)]
print(mylist3)

print("\n")
print("Adding an IF condition in the list comprehension")

mylist4 = [x for x in range(0,11) if x % 2 == 0 ]
print(mylist4)
