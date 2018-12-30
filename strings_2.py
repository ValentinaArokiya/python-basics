# .format() method and f string

print('The {} {} {}' .format('fox', 'brown', 'quick'))

print('The {2} {1} {0}' .format('fox', 'brown', 'quick'))

print('The {1} {1} {1}' .format('fox', 'brown', 'quick'))

print('The {q} {b} {f}' .format(f= 'fox', b= 'brown', q= 'quick'))

result = 100/777
print(result)

print("The result was {}" .format(result))

print("The result was {r:1.3f}" .format(r=result)) #--{value:width.precision f}

print("The result was {r:10.3f}" .format(r=result))

print("The result was {r:10.8f}" .format(r=result))

# fstring
name = "Jose"
print(f"Hello, my name is {name}")

print("{} {}" .format('Python', 'rules'))
