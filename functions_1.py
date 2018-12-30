print("Return result as a new string")

def myfunc(st):
    new_st=''
    for index,letter in enumerate(st):
        if index%2 == 0:
            new_st=new_st+letter.upper()
        else:
            new_st=new_st+letter
    return new_st

result = myfunc("abcdefghijk")
print(result)
print("\n")
#
# word = 'hello'
# upper = word.upper()
# print(upper)
#
#
#
print("Return result as a list")
def myfunc1(st):
    new_st=[]
    for index,letter in enumerate(st):
        if index%2 == 0:
            new_st.append(letter.upper())
        else:
            new_st.append(letter.lower())
    return new_st

result = myfunc1("abcdefghijk")
print(result)
