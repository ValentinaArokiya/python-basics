# range - is a generator. It generates some sort of information, instead of saving all the information to memory. More efficient system.
# range - does not include the end number

print("Range")
for num in range(10):
    print(num)

print("Start-Stop")
for num in range(3,10):
    print(num)

print("Start-Stop-Step")
for num in range(3,10,2):
    print(num)


print("To print the elements of a range, it has to be casted to a list.")
print(list(range(0,11,2)))

    