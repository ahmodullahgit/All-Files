salary = int(input("Sir, Please enter your salary: "))
years_of_service = int(input("How many years have you been in service: "))

if years_of_service > 5:
    net_bonus_amount = round(salary + (salary * 0.05))
    print("Congratulations! Your net bonus amount is", net_bonus_amount, "BDT.")
else:
    print("Oops! You're not illegible for bonus. Your salary is", salary, "BDT.")

# salary = int(input("Sir, Please enter your salary: "))
# years_of_service = int(input("How many years have you been in service: "))
#
# while True:
#     if years_of_service > 5:
#         net_bonus_amount = round(salary + (salary * 0.05))
#         print("Congratulations! Your net bonus amount is", net_bonus_amount, "BDT.")
#         break
#     else:
#         print("Oops! You're not illegible for bonus. Your salary is", salary, "BDT.")
#         continue

