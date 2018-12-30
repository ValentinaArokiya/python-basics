# LIST - [1,2,3,abc]
# LISTS support indexing and slicing
# lists are mutable. you can modify the elements of the list using the index
# you can use methods with list functions. list_a.append(), pop(), pop(2)

my_list = [1, 2, 3, 4, "abcdef", 8.23]
print(len(my_list))
print(my_list[2])
print(my_list[1:5])
print(my_list[1:])

another_list = [10, 20, 30]

print(my_list + another_list)

list_a = ['one', 'two', 'three']
list_a[0]= 'ONE'    #lists are mutable
print(list_a)
list_a.append('six')
print(list_a)

popped =list_a.pop()
print(popped)
print(list_a)

list_a.pop(0)
print(list_a)



