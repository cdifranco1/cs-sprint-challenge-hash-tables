

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_dict = {}
    
    for i, x in enumerate(weights):
        weight_dict[x] = i

    for i, x in enumerate(weights):
        if (limit - x) in weight_dict:
            first_idx = i
            second_idx = weight_dict[limit - x]
            result = (max(first_idx, second_idx), min(first_idx, second_idx))
            return result

    return None


weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
print(get_indices_of_item_weights(weights_4, 9, 7))

weights_3 = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(weights_3, 5, 21))

weights_2 = [4, 4]
print(get_indices_of_item_weights(weights_2, 2, 8))

'''
iterate through weights
put weights into dict with weight as key (limit - weight, index) as value

iterate through dict:
    if (limit - weight) in dict:
        result = current index and index of limit - weight
'''