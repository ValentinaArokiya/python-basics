# Iterating through a Dictionary

# when you iterate thru a dictionary, by default it iterates only thru the keys.
d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d:
    print(item)

# if you want to iterate through the items itself, then call d.items()
d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d.items():
    print(item)

# tuple unpacking with d.items()
d = {'k1': 1, 'k2': 2, 'k3': 3}
for key,value in d.items():
    print(value)
