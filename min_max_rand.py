# min
# max
# rand
# input - user input



from random import shuffle
from random import randint



mylist = [10, 20, 30, 40, 50]

print(min(mylist))
print(max(mylist))


(shuffle(mylist)) # -inplace function. wont return any value. None Type. The original list is shuffled.

print(mylist)


print(randint(0, 100))

print("ENTER INPUT")

name = input("Enter your name:")
print(name)

number = int(input("Enter number"))
print(number + 1)



