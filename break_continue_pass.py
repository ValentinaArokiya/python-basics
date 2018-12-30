# break - breaks out of the current closest enclosing loop. end of loop
# continue - continues to the top of the current closest enclosing loop. increments and goes to the next iteration
# pass - does nothing at all

print("PASS***********************")

x = [1, 2, 3]
for item in x:
    pass     # placeholder for the statements
print("end of script")


print("CONTINUE***********************")

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        continue
    print(letter)
print("End")

print("BREAK***********************")

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        break
    print(letter)
print("End")

print("BREAK with WHILE LOOP")

x=0
while x < 5:
    if x == 3:
        break
    print(x)
    x = x+1
