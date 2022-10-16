# Access the index number of a list

# Solve-1
nums = [5, 15, 35, 8, 98]
for num in nums:
    print(str(num).zfill(2), '-----', nums.index(num))


# Solve-2 : Using Enumerate Function
nums = [5, 15, 35, 8, 98]
for index, num in enumerate(nums):
    print(str(num).zfill(2), index, sep=' ----- ')
    # print(str(num).zfill(2), '-----', index)

