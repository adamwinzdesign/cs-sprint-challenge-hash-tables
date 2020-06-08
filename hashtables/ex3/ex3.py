# Given multiple lists of numbers, find the numbers that appear in all of the lists, in other words, output the common entries.
# There can be up to 10 lists, but each list can contain up to 1,000,000 entries.

def intersection(arrays):
    common_numbers = {'intersection': []}
    k = len(arrays)
    n = 0
    for i in range(k):
        if len(arrays[i]) > n:
            n = len(arrays[i])
    for i in range(n):
        for j in range(k):
            if i > len(arrays[j]) - 1:
                continue
            num = arrays[j][i]
            if num in common_numbers:
                common_numbers[num] += 1
                if common_numbers[num] == k:
                    common_numbers['intersection'].append(num)
            else:
                common_numbers[num] = 1

    return common_numbers['intersection']


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
