def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash = {}

    for i in range(length):
        complement = limit - weights[i]
        if complement in hash:
            return (i, hash[complement])
        hash[weights[i]] = i


    return None
