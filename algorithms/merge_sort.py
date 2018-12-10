def merge_sort(number_array):
    if len(number_array) <= 1:
        return number_array

    mid = len(number_array) // 2
    left_array = number_array[:mid]
    right_array = number_array[mid:]

    sorted_left = merge_sort(left_array)
    sorted_right = merge_sort(right_array)

    i, j, k = 0, 0, 0

    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] < sorted_right[j]:
            number_array[k] = sorted_left[i]
            i += 1
        else:
            number_array[k] = sorted_right[j]
            j += 1
        k += 1

    while i < len(sorted_left):
        number_array[k] = sorted_left[i]
        i += 1
        k += 1

    while j < len(sorted_right):
        number_array[k] = sorted_right[j]
        j += 1
        k += 1

    return number_array
