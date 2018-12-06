def insertion_sort(number_array):
    for index in range(1, len(number_array)):

        current_position = index

        while current_position > 0 and number_array[current_position - 1] > number_array[current_position]:
            number_array[current_position -
                         1], number_array[current_position] = number_array[current_position], number_array[current_position - 1]
            current_position -= 1
    return number_array
