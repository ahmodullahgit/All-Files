print("Please check, if the registration time is over or not: ")
submission_date = int(input("Enter today's date only(i.e. 06): "))
payment_status = input("Have you made full payment? - Yes/No: ")
join_status = input("When did you join the course? - On Time/Delay: ")
cashback_amount = 6000*0.15
if 2 <= submission_date < 10:
    print("Great! Go Ahead. Hope you'll get the offer. Try Next Step.")
    if payment_status == "Yes" or "yes":
        if join_status == "On Time" or "on time":
            print("Wow! Congratulations! You have got 15% cashback. The amount will be", cashback_amount,"BDT")
        #elif join_status == "Delay" or "delay":
            #print("Oops! Sorry. You're not illegible for cashback.")
        else:
            print("You don't care about instructions! That ridiculous!")
    #elif payment_status == "No" or "no":
        #print("Oops! Sorry. You're not illegible for cashback.")
    else:
        print("You don't care about instructions! That ridiculous!")

elif 10 <= submission_date <= 31:
    print()
else:
    print("Please! Follow the instructions.")