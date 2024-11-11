def binary_search(sorted_array, target):
    start = 0
    end = len(sorted_array)
    while start <= end:
            mid = (start + end) // 2

            if target == sorted_array[mid]:
                return mid
            elif target > sorted_array[mid]:
                start = mid + 1
            else:
                end = mid - 1