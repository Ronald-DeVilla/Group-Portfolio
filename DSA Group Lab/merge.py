def merge_sort(arr):
    steps = []
    if len(arr) <= 1:
        return arr, steps
    
    def merge(left, right):
      merged = []
      i = j = 0

      while i < len(left) and j < len(right):
          if left[i] <= right[j]:
              merged.append(left[i])
              i += 1
          else:
              merged.append(right[j])
              j += 1
      merged.extend(left[i:])
      merged.extend(right[j:])
      return merged

    def recursive_merge_sort(arr):
        if len(arr) <= 1:
            return arr, []
        
        mid = len(arr) // 2
        left_half, left_steps = recursive_merge_sort(arr[:mid])
        right_half, right_steps = recursive_merge_sort(arr[mid:])
        
        merged_arr = merge(left_half, right_half)
        
        steps.extend(left_steps)
        steps.extend(right_steps)
        
        steps.append(arr[:])

        
        
        steps.append(merged_arr[:])

        return merged_arr, steps

    sorted_arr, steps = recursive_merge_sort(arr)
    
    return sorted_arr, steps