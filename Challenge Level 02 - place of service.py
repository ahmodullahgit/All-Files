gender = input("Select your gender (M/F): ")
if gender == "F":
    print("Urban areas only.")
elif gender == "M":
    age = int(input("Enter your age: "))
    if 40 <= age <= 60:
        print("Urban areas only.")
    elif 20 <= age <= 39:
        print("Anywhere.")
    else:
        print("ERROR")
else:
    print("Feeling Angry! You've entered all stupid data. Enter your data according to instructions! Re-run the code.")

