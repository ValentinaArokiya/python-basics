# when you want to pass in an arbitrary number of argument, without having to pre-define a bunch of parameters in your function.

# *args - arguments - tuple of parameters. the list of arguments passed in to the function will be treated as a tuple. (1,5,7,5,3,9)
# **kwargs - keyword arguments- arguments are treated as a dictionary of key:value pairs {'key1':'value1','key2':'value2'}


def myfunc(a,b):
    return sum((a,b)) * 0.5
result = myfunc(40,60)
print(result)



print("More parameters included:")

def myfunc2(*args):
    return sum(args) * 0.5
result_2= myfunc2(2,3,5,1,7,9)
print(result_2)
print("\n")

print("----------*args------")
def myfunc3(*args):
    print(args)
myfunc3(2,8,7,5,90,56,5,12)

print("\n")
print("----------**kwargs------")
def myfunc4(**kwargs):
    print(kwargs)

    for num in args:
        if num%2==0:
            even_num.append(num)
    return even_num

even = myfunc6(1,2,4,7,9,45,32,13,88)
print(even)
