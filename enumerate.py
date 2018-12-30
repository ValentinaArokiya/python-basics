# enumerate is used to get the index and the element in a loop

# zip - zips together 2 or more lists

# in - to see if an object is in a list

print("ENUMERATE***********************************")
word = 'abcde'

for item in enumerate(word):
    print(item)

print("________________________________")
print('\n')

word = 'abcde'

for index, letter in enumerate(word):
    print(index, letter)



print('\n')
print("ZIP***************************************")
mylist1 = [1,2,3]
mylist2 = ['a', 'b', 'c']
for item in zip(mylist1,mylist2):
    print(item)


print("\n")
print("ANOTHER ZIP***************************************")
# uneven lists:
# if there are more elements in one list than other lists, the extra elements will be ignored. Only goes as far as the shortest list.
mylist1 = [1,2,3,4,5]
mylist2 = ['a', 'b', 'c', 'd']
mylist3 = [100, 200, 300]
for item in zip(mylist1,mylist2,mylist3):
    print(item)



# Casting a zip:
print(list(zip(mylist1,mylist2,mylist3)))

print("______________________________________________")
print("\n")
print("IN")
print('x' in [1,2,3,4])
print('x' in ['x', 'y', 'z'])


