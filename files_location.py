# myfile = open("User/YourUserName/Folder/myfile.txt

# when using the with open command, you dont have to close() the file.

# mode = 'r' is read only
# mode = 'w' is write only. Will overwrite files or create a new one
# mode = 'a' is append only. Will add on to files.
# mode = 'r+' is reading and writing
# mode = 'w+' is writing and reading. Will overwrite existing files or create new one.
with open('file1.txt') as my_new_file:
    contents = my_new_file.readlines()
    print(contents)

with open('file1.txt', mode='r') as my_new_file:
    contents = my_new_file.read()
    print(contents)

print("@@@@@@")

with open('file2.txt', mode = 'r') as f:
    print(f.read())
print("@@@@@")

with open('file2.txt', mode='a') as f:
    f.write("Four on Fourth")
print("@@@@")
with open('file2.txt', mode = 'r') as f:
    print(f.read())

#WRITE TO FILE: python created this file:
print("&&&&&&&&&&")
with open('xyz.txt', mode = 'w') as f:
    f.write("I just created this file")

with open('xyz.txt', mode = 'r') as f:
    print(f.read())


