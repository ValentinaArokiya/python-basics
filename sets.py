# SETS - unordered and unique elements {1, 2, 3, 'a'}
# no duplicates
# .add()

myset = set()
myset.add(1)
print(myset)
myset.add(2)
print(myset)
myset.add(2) # has to be unique. wont repeat values.
print(myset)


# casting set:

mylist = [1,1,1,1,2,2,2,3,3,3,4,4,4,4]
myset1 = set(mylist)
print(myset1)

print(set("Mississippi"))
