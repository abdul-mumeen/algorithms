def get_split_point(number_list, first_index, last_index):
    pivot_value = number_list[first_index]

    left_position = first_index + 1
    right_position = last_index

    done = False
    while not done:

        while left_position <= right_position and number_list[left_position] <= pivot_value:
            left_position = left_position + 1

        while number_list[right_position] >= pivot_value and right_position >= left_position:
            right_position = right_position - 1

        if right_position < left_position:
            done = True
        else:
            number_list[left_position], number_list[right_position] = number_list[right_position], number_list[left_position]

    number_list[first_index], number_list[right_position] = number_list[right_position], number_list[first_index]

    return right_position


def quick_sort_recursion(number_list, first_index, last_index):
    if first_index < last_index:

        split_point = get_split_point(number_list, first_index, last_index)

        quick_sort_recursion(number_list, first_index, split_point - 1)
        quick_sort_recursion(number_list, split_point + 1, last_index)


def quick_sort(number_list):
    quick_sort_recursion(number_list, 0, len(number_list) - 1)
    return number_list
