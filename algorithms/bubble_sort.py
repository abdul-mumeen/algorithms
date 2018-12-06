def bubble_sort(number_array):
    array_len = len(number_array)
    while array_len > 0:
        for index in range(array_len - 1):
            if number_array[index] > number_array[index + 1]:
                number_array[index], number_array[index +
                                                  1] = number_array[index + 1], number_array[index]
        array_len -= 1

    return number_array
