# iterable
# you know beforehand how many times to iterate.
# execute the block of code for every iteration

my_iterable = [1,2,3]
for item in my_iterable:
    print(item)

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print("Even-Odd")
list_num = [1,2,3,4,5,6,7,8,9,10]
for num in list_num:
    if num % 2 == 0:
        print(num)
    else:
        print(f"Odd {num}")

print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
print("SUM")

list_a = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for n in list_a:
    sum = sum + n
    print(sum)

print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
print("Iterating through list")
list_a = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for n in list_a:
    sum = sum + n
print(sum)

print("STRING-ITERATION******************************")
for letter in "Hello World":
    print(letter)

print("Iterating through tuple")
tup = (1,2,3)
for item in tup:
    print(item)

print("LIst of tuples")
my_list = [(1,2),(3,4),(5,6),(7,8)]
for item in my_list:
    print(item)

print("Tuple unpacking")
my_list = [(1,2),(3,4),(5,6),(7,8)]
for a,b in my_list:
    print(a)
    print(b)

print("ONE MORE TUPLE UNPACKING")

my_list = [(1, 2, 3), (3, 4, 5), (5, 6, 7), (7, 8, 9)]
for a, b, c in my_list:
    print(b)
    print(c)




