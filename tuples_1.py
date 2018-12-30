# Tuples are immutable
# can perform indexing and slicing
# index() and count()

t = (1,2,3)    # tuple
l = [1,2,3]    # list

print(type(t))
print(type(l))

print(len(t))


t1 = ('one', 2, 3.5, 4, 5.0, 6, 7, 2)
print(t1)

print(t1[1:4])
print(t1[-1])
print(t1.count(2))
print(t1.index(2))

tuple_1 = (1, 2, 3, 4)
list_1 = [1, 2, 3, 4]

list_1[0] = "New"
print(list_1)

# tuple_1[0] = "NEW"   # cannot change a value of tuple
