
i = 0
while True:
    number = int(input('Enter any number: '))
    if number % 2 == 0:
        print('Your given number', number, 'is an even number.')
        continue
    else:
        print('Your given number', number, 'is an odd number.')
        i = i + 1
        ask = input('Type "Quit" to Exit or Press "Enter" to Continue: ')
        if ask.title() == "Quit":
            break