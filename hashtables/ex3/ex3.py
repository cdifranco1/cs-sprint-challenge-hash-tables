def intersection(arrays):
    """
    YOUR CODE HERE
    """
    total = len(arrays)
    counter = {}
    result = []

    for arr in arrays:
        for x in arr:
            if x in counter:
                counter[x] += 1
            else:
                counter[x] = 1
    
    for key, value in counter.items():
        if value == total:
            result.append(key)
    
    return result

# # V2
# def intersection(arrays):
#     """
#     YOUR CODE HERE
#     """
#     counter = {}
#     for i in range(len(arrays)):
#         counter[i] = [] 
#     counter[0] = arrays[0]

#     for i in range(0, len(arrays) - 1):
#         counter_arr = counter[i]
#         next_arr = arrays[i + 1]
#         for num in counter_arr:
#             if num in next_arr:
#                 counter[i + 1].append(num)        
    
#     return counter[len(arrays) - 1]

# print(intersection([
#             [1,2,3],
#             [1,4,5],
#             [1,6,7]
#         ]))


# First implementation

# count total number of arrays
# store each number in dict with array count
# iterate through dict items:
#   if array count = num arrays:
#       push key to result     

# Faster implementation

# create dict
# add index as key for each arr in outer arr with empty arr as value
# for nums in first arr:
#   add num to dict[0]
# iterate through dict[0]:
#   if num is in arr[1]:
        # move num from dict[0] to dict[1]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
