# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald
#
# Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(name):
    new_name = ''
    for index,letters in enumerate(name):
        if index == 0 or index == 3:
            new_name = new_name + letters.upper()
        else:
            new_name = new_name + letters
    return new_name

result = old_macdonald("macdonald")
print(result)



print("Method-2")
# .capitalize() - capitalizes only the first letter of every word in the string


