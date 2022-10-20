# Find leap year:
"""
year = int(input('Enter a year: '))
if year % 4 == 0:
    print('Great! You entered a leap year.')
else:
    print("Oops! You didn\'t enter leap year.")
"""
# Find Upcoming leap year
"""  # Problem found
year = int(input('Enter your year: '))
i = 2022
result = 0
while i <= year:
    if i % 4 == 0:
        result = result + 1
        break
    i += 1

if result == 1:
    print('Leap year found successfully!')
else:
    print('Can\'t find any leap year.')
"""
"""
year_outline = int(input('Enter your year outline: '))
i = 2022
blank_list = []
while i <= year_outline:
    if i % 4 == 0:
        blank_list.append(True)
    else:
        blank_list.append(False)
    i += 1

if True in blank_list:
    print('Leap year found successfully!')
else:
    print('Can\'t find any leap year.')
"""

"""
i = 0
while True:
    year = int(input('Enter a year: '))
    if year % 4 == 0:
        print('Great! You entered a leap year.')
        to_continue = input("Press 'Enter' to continue: ")
        i += 1
        continue
    else:
        print("Oops! You didn\'t enter leap year.")
        to_break = input("Press 'Enter' to Exit: ")
        break
"""
"""
i = 0
while True:
    year = int(input('Enter a year: '))
    if year % 4 == 0:
        print('Great! You entered a leap year.')
        i += 1
        continue
    else:
        print("Oops! You didn\'t enter leap year.")
"""
"""
i = 0
while True:
    year = int(input('Enter a year: '))
    if year % 4 == 0:
        print('Great! You entered a leap year.')
        i += 1
        continue
    else:
        print("Oops! You didn\'t enter leap year.")

    ask = input('Type "Quit" to Exit or Press "Enter" to Continue: ')
    if ask.title() == "Quit":
        break
"""
"""
i = 0
result = 0
while i <= year:
    if i % 4 == 0:
        result = result + 1
        break
    i += 1

if result == 1:
    print('Leap year found successfully!')
else:
    print('Can\'t find any leap year.')
"""
start = int(input('Enter your start year: '))
end = int(input('Enter your end year: '))
result1 = 0
result2 = 0
i = start
while i <= end:
    if i % 4 == 0:
        result1 = result1 + 1
    else:
        result2 = result2 + 1
    i = i + 1
print(f'Leap year: {result1}')
print(f'Not leap year: {result2}')
