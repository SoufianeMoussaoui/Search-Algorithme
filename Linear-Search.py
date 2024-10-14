def linear_search(arr, target):
    # 1. Initialization: Start at the first element of the list (index 0)
    for index in range(len(arr)):
        # 2. Comparison: Compare the current element with the target
        if arr[index] == target:
            # 3. Check for Match: If a match is found, return the index
            return index
    
    # 5. End of List: If the target is not found, return -1 indicating it's not in the list
    return -1

