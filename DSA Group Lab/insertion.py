def insertion_sort(arr):
    steps = []
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        temp_arr = arr[:]
        steps.append(temp_arr)
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            temp_arr = arr[:]
            steps.append(temp_arr)
        arr[j + 1] = key
        temp_arr = arr[:]
        steps.append(temp_arr)
    return arr, steps