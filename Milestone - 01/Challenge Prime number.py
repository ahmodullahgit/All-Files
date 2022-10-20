number = int(input("Enter any number: "))
i = 2
blank_list = []
while i < number > 1:
    if number % i == 0:
        blank_list.append(False)
    else:
        blank_list.append(True)
    i += 1
if all(blank_list) == True:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number.")

