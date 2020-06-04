# Given multiple lists of numbers, find the numbers that appear in all of the lists, in other words, output the common entries.
# There can be up to 10 lists, but each list can contain up to 1,000,000 entries.

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
