"""
Write a python programme to print a specified list after removing the 0th, 4th and 5th elements.
sample list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected output: sample list = ['Green', 'White', 'Black']
"""

# Solution - 1:
sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

sample_list.pop()
sample_list.pop()
sample_list.pop(0)
print(sample_list)

"""
# Solution - 2:
sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
sample_list = [color for (i,color) in enumerate(sample_list) if i not in (0,4,5)]
print(sample_list)
"""
"""
languages = ['Python', 'Java', 'JavaScript']
enumerate_result = enumerate(languages, 100)
print(list(enumerate_result))
"""
"""
for text in enumerate('hello'):
    print(text)
"""

sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
sample_list = [color for index,color in enumerate(sample_list) if index not in (0,4,5)]
print(sample_list)

sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
sampleList = []
for index, color in enumerate(sample_list):
    if index not in (0,4,5):
        sampleList.append(color)
print(sampleList)
