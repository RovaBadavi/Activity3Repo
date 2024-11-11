def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[ :mid]
        right = array[mid: ]

        merge_sort(left)
        merge_sort(right)

        l = 0
        r = 0 
        a = 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                array[a] = left[l]
                l = l + 1
            else:
                array[a] = right[r]
                r = r + 1
            a = a + 1
        while l < len(left):
            array[a] = left[l]
            l = l + 1
            a = a + 1
        while r < len(right):
            array[a] = right[r]
            r = r + 1
            a = a + 1