nums = [3, 1, 0, 2, 2, 1, 5, 1, 7, 8, 0, 67, 1, 3, 4]
print([*filter(lambda x: x != 0, nums)]+[*filter(lambda x: x == 0, nums)])