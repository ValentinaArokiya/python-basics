# text files - .txt file shd be saved in the same location as the python program.
# to open a file, the file should exist in the same location.
# if you try to open a file that does not exist, you would see a FileNotFoundError. Also same error is displayed when the file is in a different directory.
# you could write to a file that does not exist. Python would create the file and write to it.

# read() - outputs the file as 1 giant string.
# readlines() - outputs the file as a list of lines - ['line1\n', 'line2\n', 'line3\n']
# seek(0)
# close()

myfile = open('file1.txt')

print(myfile.read())
myfile.seek(0) # after you read th file once, you try to read again and you get an empty string. When you read the
# file for the first time, the cursor is at the end of the file. You need to reset the cursor back to the beginning of
# file in order to read it again.

print(myfile.read())

myfile.seek(0)

print(myfile.readlines())

myfile.close()

# myfile = open('file2.txt')

