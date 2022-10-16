number = 2
while number <= 100:
    counter = 0
    i = 1
    while i <= number:
        if number % i == 0:
            counter = counter + 1
        i = i + 1
    if counter == 2:
        print(number, end = " ")
    number = number + 1
