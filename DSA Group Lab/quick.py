def quick_sort(arr):
    steps = []

    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            temp_arr = arr[:]
            steps.append(temp_arr)
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                temp_arr = arr[:]
                steps.append(temp_arr)
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        temp_arr = arr[:]
        steps.append(temp_arr)
        return i + 1
            

    def recursive_quick_sort(arr, low, high):
        if low < high:
            partition_index = partition(arr, low, high)
            recursive_quick_sort(arr, low, partition_index - 1)
            recursive_quick_sort(arr, partition_index + 1, high)
        
        
    recursive_quick_sort(arr, 0, len(arr) - 1)
    
    temp_arr = arr[:]
    steps.append(temp_arr)
    
    return arr, steps