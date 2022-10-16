# Write a python programme to insert a given string at the beginning of all item in a list
# Sample list = [1, 2, 3, 4] , String = 'emp'
# Expected Output: [emp1, emp2, emp3, emp4]
sample_list = [1, 2, 3, 4]
string_ = 'emp'
new_list = []
for newlist in sample_list:
    result = 'emp'+ str(newlist)
    new_list.append(result)
print(new_list)

sample_list = ['emp' + str(newlist) for newlist in sample_list]
print(sample_list)

