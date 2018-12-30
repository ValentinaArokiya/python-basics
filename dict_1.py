# unordered and cannot be sorted
# has key-value pairs
# list - are retrieved by location. So can use index and slicing.

prices_lookup = {'apple' : 2.99, 'grapes' : 4.99, 'orange' : 3.05}
print(prices_lookup['grapes'])   # instead of passing the index position, we pass in the key itself.


print(prices_lookup)

d = {'k1': 123, 'k2': 456, 'k3': {'key1': 100}, 'k4': 'c'}

print(d['k2'])
print(d['k3'])
print(d['k3']['key1'])
# (d['k4'][0]).upper()
# print(d)

e = {'k1': 100, 'k2': 200, 'k3' : 300}
print(e)
e['k7'] = 700    # adding key value pair to existing dictionary
print(e)
e['k1'] = 1000   # modifying the existing value of a key
print(e)

print(e.keys())
print(e.values())
print(e.items())    # result will be in the form of tuples
