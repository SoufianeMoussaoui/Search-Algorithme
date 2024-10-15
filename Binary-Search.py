def binary_search(arr, target):
    # Make sure the list is sorted for binary search to work
    arr.sort()
    
    # 1. Initialization: Define the start and end indices
    left = 0
    right = len(arr) - 1

    # 2. Repeat until the search space is exhausted
    while left <= right:
        # 3. Find the middle index
        middle = (left + right) // 2
        
        # 4. Compare the middle element with the target
        if arr[middle] == target:
            # If the middle element matches the target, return the index
            return middle
        elif arr[middle] < target:
            # If the target is greater, ignore the left half
            left = middle + 1
        else:
            # If the target is smaller, ignore the right half
            right = middle - 1

    # 5. If we reach here, the target is not in the list
    return -1

