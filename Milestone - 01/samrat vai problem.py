# 1 to 100 prime number

number = 2
while number <= 100:
    i = 2
    blank_list = []
    while i < number > 1:
        if number % i == 0:
            blank_list.append(False)
        else:
            blank_list.append(True)
        i += 1
    if all(blank_list) == True:
        print(number, end=" ")
    number = number + 1
