example = 'ↁ'
example2 = '2²'
example3 = '3'

print(example3.isnumeric())    # True
print(example3.isdigit())      # True
print(example3.isdecimal())    # True

print(example2.isnumeric())    # True
print(example2.isdigit())      # True
print(example2.isdecimal())    # False

print(example.isnumeric())    # True
print(example.isdigit())      # False
print(example.isdecimal())    # False
