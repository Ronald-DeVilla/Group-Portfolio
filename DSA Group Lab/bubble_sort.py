def bubble_sort(arr):
    n = len(arr)
    steps = []
    for i in range(n):
        for j in range(0, n - i - 1):
            temp_arr = arr[:]
            steps.append(temp_arr)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                temp_arr = arr[:]
                steps.append(temp_arr)
        
    temp_arr = arr[:]
    steps.append(temp_arr)
    return arr, steps