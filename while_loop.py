# number of times to iterate is not known
# continues to execute a block of code while some condition remains true.

 # while some_boolean_condition:
    # do something

# a for loop will pick every element in the list automatically and continues the next iteration. No need to increment.
# a while loop needs to be incremented inorder to continue with the next iteration.

x=0
while x < 5:
    print(f"The current value of x is {x}")
    x = x+1
else:
    print("X is not less than 5")
    