# built-in methods
# Functions
# whatever information you provide in docstrings will be displayed in the Help file for the function.
# if a function has a print stmt...it will just print the o/p when the function is called. No further operations can be performed with the o/p.

# if a function has a return stmt...it will return the o/p and assign it to a variable, when the function is called.
# the returned o/p can be used to perform some operations.
print("built-in methods")
mylist = [1,2,3]

help(mylist.insert)
print("\n")

print("Functions")

def name_of_function(name):
    '''
    docstring:
    Input: name
    Output: Hello <name>
    :return:
    '''
    print("Hello!" + name)



print("\n")
name_of_function("Tina")
print("\n")
print("________________________________________________________")

help(name_of_function)
print("\n")
print("RETURN STMT:")
print("________________________________________________________")

def add_function(num1,num2):
    return num1+num2
result=add_function(3,5)
print(result*10)
print("________________________________________________________")
print("\n")

print("Default Parameter")
def say_hello(name = "NAME"):
    print('Hello ' + name)
say_hello("Jaydon")
say_hello()
print("________________________________________________________")
print("\n")


print("FUNCTION-2")
def dog_check(mystring):
    if 'dog' in mystring:
        return True
output = dog_check("I have a pet dog")
print(output)

print("Same as Function-2 but more efficient programming:")
def dog_check(mystring):
    return 'dog' in mystring.lower()

output = dog_check("I have a pet Dog")
print(output)

print("________________________________________________________")
print("\n")


print("FUNCTION-3: PIG LATIN")
def pig_latin(word):
    if word[0] in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + word[0] + 'ay'
    return pig_word
w = pig_latin("fellolephant")
print(w)

