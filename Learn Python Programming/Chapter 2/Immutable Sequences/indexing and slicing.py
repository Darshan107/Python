# Indexing: get data from one precise position
# Slicing: get a subsequence from sequenced data
# in case of immutable data, they are read only.

def indexing_slicing():
    # Indexing
    my_list = [1, 2, 3, 4, 5]
    print(f'{my_list = }')
    print(f'First element: {my_list[0]}')  # Output: 1, indexing starts from 0
    print(f'Last element: {my_list[-1]}')  # Output: 5, negative indexing starts from  -1 and denotes the last item, -2 would be second last.
    print(f'Second element: {my_list[1]}')  # Output: 2
    # Slicing
    print(f'Elements from index 1 to 3: {my_list[1:4]}')  # Output: [2, 3, 4], slicing have 3 data points [start:end:step]
    print(f'Elements from index 2 to end: {my_list[2:]}')  # Output: [3, 4, 5]
    print(f'Elements from index 0 to 2: {my_list[:3]}')  # Output: [1, 2, 3]
    print(f'Elements from index -3 to -1: {my_list[-3:-1]}')  # Output: [3, 4], negative step means going backwards
    print(f'Elements in reverse order: {my_list[::-1]}')  # Output: [5, 4, 3, 2, 1]
    print(f'Elements in reverse order, skipping every second: {my_list[::-2]}')  # Output: [5, 3, 1]

indexing_slicing()