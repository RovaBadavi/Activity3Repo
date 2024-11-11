import time, random

def merge_sort(array):
    """
    This function performs merge sort on an array that is input into it

    Args:
    array - This is the array that is inputted into the function

    Output:
    There is no output as this functions sorts the array in place
    """
    if len(array) > 1: #base case
        mid = len(array) // 2
        left = array[ :mid] #array from the left
        right = array[mid: ] #array from the right

        merge_sort(left)
        merge_sort(right)

        l = 0 #index of left side
        r = 0 #index of right side
        a = 0 #index of the main array

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                array[a] = left[l]
                l = l + 1
            else:
                array[a] = right[r]
                r = r + 1
            a = a + 1
        while l < len(left): # other elements from left array
            array[a] = left[l]
            l = l + 1
            a = a + 1
        while r < len(right): # other elements from right array
            array[a] = right[r]
            r = r + 1
            a = a + 1

def generate_sorted_data(size):
    """
    This function generates a sorted array, it generates a random array and makes use of merge sort

    Args:
    size - This will be roughly the size of the array, as there are 10 extra numbers present

    Output:
    array - Returns a sorted random array
    """
    array = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44] + [random.randint(1, 100) for x in range(size)]
    merge_sort(array)
    return array

def binary_search(sorted_array, target):
    """
    This function uses binary search to find a target value in a sorted array

    Args:
    sorted_array - An array that is already sorted
    target - The value that is being searched for in the array

    Output:
    mid - This is the index of the targeted value
    """
    start = 0 # starting point
    end = len(sorted_array) # ending point
    while start <= end: 
            mid = (start + end) // 2 # to find the middle element

            if target == sorted_array[mid]: # returns target when if the middle element is the target value
                return mid
            elif target > sorted_array[mid]:
                start = mid + 1 # when target is greater it ignores all the left elements
            else:
                end = mid - 1 #  when target is smaller it ignores all the rights elements

def linear_search(array, target):
    """
    This function uses linear search to find a target value in a sorted array

    Args:
    array - An array, does not have to be sorted
    target - The value that is being searched for in the array

    Output:
    index - This is the index of the targeted value
    """
    for index in range(len(array)):
        if array[index] == target: # the value that the index is holding is the target
            return index

def main():
    data = generate_sorted_data(100000) # generating a sorted array of a specific size
    target = 90 # the value that is being targeted

    # calculating the time for binary search
    start_binary = time.perf_counter() # start time
    return_index_binary = binary_search(data, target)
    end_binary = time.perf_counter() # end time
    duration_binary = end_binary - start_binary # time taken
    print(return_index_binary)
    print(f"The time taken for binary search was {duration_binary} seconds")

    # calculating the time for linear search
    start_linear = time.perf_counter() # start time
    return_index_linear = linear_search(data, target)
    end_linear = time.perf_counter() # end time
    duration_linear = end_linear - start_linear # time taken
    print(return_index_linear)
    print(f"The time taken for linear search was {duration_linear} seconds")

    # if statement to summarize the time calculations
    if duration_binary > duration_linear:
        print(f"Linear search was faster by a factor of {duration_binary/duration_linear:.2f}x")
    elif duration_linear > duration_binary:
        print(f"Binary search was faster by a factor of {duration_linear/duration_binary:.2f}x")

if __name__ == "__main__":
    main()





