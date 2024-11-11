import random

#small_data = [random.randint(1, 100) for n in range(10)]
small_data = [34, 7, 23, 32, 5, 62, 29, 12, 40, 8]
def generate_sorted_data(size):
    for index in reversed(range(len(size))):
        key = size[index] 

        sub_index = index + 1
        while sub_index < len(size) and size[sub_index] < key:
            size[sub_index - 1] = size[sub_index]
            sub_index = sub_index + 1

        size[sub_index - 1] = key
    