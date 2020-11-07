def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    numbers = {}

    for i in range(len(a)):
        if a[i] > 0:
            numbers[a[i]] = i
    for i in range(len(a)):
        if a[i] < 0:
            if (-a[i]) in numbers:
                result.append(-a[i])

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
