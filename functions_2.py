# FUNCTION PRACTICE EXERCISE:
# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd

def lesser_of_two(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)

result = lesser_of_two(2,24)
print(result)



