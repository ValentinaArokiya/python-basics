# Celcius to Fahrenheit

print("Celcius to Fahrenheit using basic for loop:")
celcius = [0, 10, 20, 30, 40, 50.5]

fahrenheit = []
for temp in celcius:
    fahrenheit.append((9/5)*temp + 32)
print(fahrenheit)

print("\n")
print("------------------------------------------------------------")


print("Celcius to Fahrenheit using list comprehensions:")
celcius = [0, 10, 20, 30, 40, 50.5]

fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

