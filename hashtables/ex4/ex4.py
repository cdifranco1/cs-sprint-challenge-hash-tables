def has_negatives(a):
    """
    YOUR CODE HERE
    """
    positives = {}
    result = []

    for x in a:
        if x > 0:
            positives[x] = False

    for x in a:
        if x < 0:
            if (-1 * x) in positives:
                positives[-1 * x] = True

    for key, value in positives.items():
        if value is True:
            result.append(key)
        
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
