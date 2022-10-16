cost_per_unit = 100
quantity_of_purchase = int(input("How many units did you buy: "))
cost_without_discount = cost_per_unit * quantity_of_purchase
total_cost_for_user = round(cost_without_discount - (cost_without_discount * 0.1))

if cost_without_discount > 1000:
    print("Congratulations! Your total cost with discount is", total_cost_for_user, "BDT.")
else:
    print("Oops! You're not illegible for discount. Your cost with no discount is", cost_without_discount, "BDT.")
