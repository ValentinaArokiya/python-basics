# #Example-1:
#
# x = 50
#
# def func(x):
#     print(f'X is {x}')
#
# func(x)
#

# #Example-2:
#
# x = 50
#
# def func(x):
#     print(f'X is {x}')
#
#     x = 200
#     print(f'I just locally changed X to {x}')
#
# func(x)
#
# print(x)

#Example-3: the value of x which is defined outside the function can be changed, using the global keyword

x = 50

def func():
    global x  # grab the value of the global x, and do whatever changes you want to x.
    print(f'X is {x}') # just print the value of x.

    x = 200 # assign a new value to the variable x. Local reassignment on a global variable
    print(f'I just locally changed X to {x}')

print(x) # this will print the original value of x, since the value isnt changed yet.
func()

print(x)  # this will print the new value of x, that got changed by the function.



