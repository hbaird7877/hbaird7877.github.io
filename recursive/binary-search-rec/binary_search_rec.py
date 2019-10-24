
def binary_search(num, arr, lower = 0, upper = -1):
    if upper == -1:
        upper = len(arr)-1
    if upper > lower:
        middle_index = lower + (upper - 1) // 2
        if arr[middle_index] == num: 
            return middle_index
        elif arr[middle_index] > num:
            return binary_search(num, arr, lower, middle_index - 1)
        else:
            return binary_search(num, arr, middle_index + 1, upper)
    elif arr[upper] == num:
        return upper
    else: return -1