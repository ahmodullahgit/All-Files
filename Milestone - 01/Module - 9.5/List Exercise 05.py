# Write a python programme to extend a list without append
# sample data = [10, 20, 30] [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]
# sort it descend

list1 = [10, 20, 30]
list2 = [40, 50, 60]
list2.extend(list1)
print(list2)
list2.sort(reverse=True)
print(list2)
