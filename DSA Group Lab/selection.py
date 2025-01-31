def selection_sort(arr):
    steps = []
    n = len(arr)
    for i in range(n):
      temp_arr = arr[:]
      steps.append(temp_arr)
      min_idx = i
      for j in range(i+1, n):
        if arr[j] < arr[min_idx]:
          min_idx = j
          
      if min_idx != i:
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        temp_arr = arr[:]
        steps.append(temp_arr)
    temp_arr = arr[:]
    steps.append(temp_arr)
    return arr, steps