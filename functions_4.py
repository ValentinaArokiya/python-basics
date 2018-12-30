# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False
# both methods are correct:
print("Method 1")
# def makes_twenty(a,b):
#     if (a + b) == 20:
#         return True
#     elif a == 20 or b == 20:
#         return True
#     else:
#         return False
#
# result = makes_twenty(120,5)
# print(result)
#
print("Method 2")


def makes_twenty(a,b):
    return (a + b) == 20 or a == 20 or b == 20

result = makes_twenty(10,10)
print(result)
