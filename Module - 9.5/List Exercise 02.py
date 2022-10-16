# Print the number of a specified list after removing even numbers from it.
num = [7, 8, 120, 25, 44, 20, 27]

# Option - 1
newlist = []
for odd_num in num:
    if odd_num % 2 != 0:
        newlist.append(odd_num)
print(newlist)

# Option - 2
num = [odd_num for odd_num in num if odd_num % 2 != 0]
print(num)