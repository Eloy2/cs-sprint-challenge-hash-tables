def intersection(arrays):
    """
    The function simply counts the amount of times a number appears in an array.
    The number is stored as a key in the table and the amount of times it appears is
    the value of the key. If the amount of times the number shows up is equal to 
    the amount of arrays in the array of arrays. Then that means the number was found in each array.
    NOTE: This only works because each number only shows up once on each array.
    """
    table = {}
    result = []
    for i in arrays: # Loop through array of arrays
        for j in i: # Loop through each value in each array
            if j in table: # check is number is in table
                table[j] += 1 # add 1 to counter
                if table[j] == len(arrays): # check if counter of number is equal to the length of array
                    result.append(j)        # if it is then that means that the number was present in all arrays in the list of arrays
            else:                           # so we append it to our result array
                table[j] = 1 # if number is not in table. add it to table and set "counter" or value to one
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
