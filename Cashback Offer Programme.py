print("----------------------------------------------------------------------")
print("Welcome To CashBack Offer Programme. Check Registration Expiry First.")
print("----------------------------------------------------------------------")

date = int(input("Enter today's date(such as- 2,3,4 etc): "))

if 2 <= date <= 9:
    print("Great! Go Ahead. Hope you'll get the offer. Go to Next Step.")
    payment_status = input("Have you made full payment? - Yes/No: ")
    if payment_status == "Yes":
        join_status = input("When did you join the course? - On Time/Delay: ")
        if join_status == "On Time":
            print("Wow! Congratulations! You have got 15% cashback. The amount will be", 6000*0.15, "BDT")
            print("Are you exited to fill up this form? The form link is in below.")
            print(r'https://nigar.pythonanywhere.com/')
            print(input("Leave your Comment here : "))
        else:
            print("Oops! Sorry. You're not illegible for cashback.")
    else:
        print("Oops! Sorry. You're not illegible for cashback.")
elif 10 <= date <= 31:
    print("Oops! Registration time is over!")
elif date == 1:
    print("Yep! Date Before Registration!")
else:
    print("You don't care about instructions! That ridiculous!")

