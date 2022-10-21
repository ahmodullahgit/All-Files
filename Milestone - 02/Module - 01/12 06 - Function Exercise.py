# Solution: Write a Python function to multiply all the numbers in a list.
numbers = [2, 6, 9, 8, 8, 15, 1, 5, 88]

"""
def multiply(list):
    multiplication = 1
    for number in list:
        multiplication *= number
    return multiplication

result_ = multiply(numbers)
print(result_)
"""

# Write a Python function that takes a number as a parameter and check the number is prime or not.
"""
def check_prime(number):
    count = 0
    i = 1
    while i <= number:
        if number % i == 0:
            count += 1
        i += 1
    if count == 2:
        print("prime")
    else:
        print("not prime")
        
check_prime(71)
"""
"""
number = 75
count = 0
for i in range(1, number+1):
    if number % i == 0:
        count += 1
if count == 2:
    print('prime')
else:
    print('not prime')
"""

def check_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
            i = i + 1
        else:
            return True

print(check_prime(23))
