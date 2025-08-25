def highest_specific_sub_array_sum(arr:list, sub_array_length: int) -> int:
    arr_lenght = len(arr)
    highest_sum = 0

    for i in range(arr_lenght - sub_array_length):
        new_sum = sum(arr[i:i + sub_array_length])
        highest_sum = max(highest_sum, new_sum)

    return highest_sum

def max_sub_array_sum(arr: list) -> int:
    arr_len = len(arr)
    max_sum = arr[0]
    max_ending = arr[0]

    for i in range(1, arr_len):
        max_ending = max(max_ending + arr[i], arr[i])
        max_sum = max(max_ending, max_sum)
    return max_sum

def missing_number(arr: list) -> int:
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    given_sum = sum(arr)
    return expected_sum - given_sum
