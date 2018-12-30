print("Program 1: split")
st = 'Print only the words that start with s in this sentence'

split_st = st.split()
print(split_st)


# list_a = list(st)   casting will separate each character by character....instead of word by word. So cant use this.
# print(list_a)
# #
for word in split_st:
    if word[0] == 's' or word[0] == 'S':
        print(word)

# print(st.split('s'))
#
print("\n")

print("Program 2: range")
even = [num for num in range(0,11) if num % 2 == 0]
print(even)
print("\n")
print("Program 3: list comprehension")

result = [num for num in range(1,51) if num % 3 == 0]
print(result)

print("\n")

print("Program 4: string")
st = 'Print every word in this sentence that has an even number of letters'

split_st = st.split()
print(split_st)


for word in split_st:
    if len(word) % 2 == 0:
        print(word)

print("\n")

print("Program 5: string")

#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".range(1,101):
print(range(1,101))
print(list(range(1,101)))

for num in range(1,20):
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    if num % 3==0:
        print("Fizz")
    elif num % 5==0:
        print("Buzz")
    else:
        print(num)

print("\n")

print("Program 6: string")

st = 'Create a list of the first letters of every word in this string'
split_st = st.split()
for word in split_st:
    print(word[0])
print("\n")


print("Program 7: same as Program 6 but with list comprehension")
st = 'Create a list of the first letters of every word in this string'
first_letter = [word[0] for word in st.split()]
print(first_letter)




