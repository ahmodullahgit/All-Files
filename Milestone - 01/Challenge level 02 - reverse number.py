number = int(input("Enter a 4-digits number: "))  # User input - for example : 1234
reverse_number = 0  # Initialization
while number > 0:  # while 1234 > 0 :      -True and loop is on
    digit_after_modulus = number % 10
    # 4 = 1234 % 10
    # 3 = 123 % 10
    # 2 = 12 % 10
    # 1 = 1 % 10
    reverse_number = (reverse_number * 10) + digit_after_modulus
    # reverse_number = (0 * 10) + 4 = 0 + 4 = 4
    # reverse_number = (4 * 10) + 3 = 40 + 3 = 43
    # reverse_number = (43 * 10) + 2 = 430 + 2 = 432
    # reverse_number = (432 * 10) + 1 = 4320 + 1 = 4321
    number = number // 10  # Update : প্রতি বার নাম্বাের ফ্লোর ডিভিশন হবে
    # (1234 // 10 = 123);
    # (123 // 10 = 12);
    # (12// 10 = 1);
    # (1 // 10 = 0) : (0 jokhon loop er condition a jabe condition true hobe na loop break hobe.)
print(reverse_number)

print(r'source: https://www.geeksforgeeks.org/write-a-program-to-reverse-digits-of-a-number/', r'source2: https://www.programiz.com/python-programming/examples/reverse-a-number')
