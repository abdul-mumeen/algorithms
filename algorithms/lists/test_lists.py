from algorithms.lists.lists import highest_specific_sub_array_sum, max_sub_array_sum, missing_number

def test_highest_specific_sub_array_sum():
    example_1 = [2, 4, 8, -1, 8, 4, 3, 34, -32]
    expected_result_1 = 41
    result_1 = highest_specific_sub_array_sum(example_1, 3)
    assert expected_result_1 == result_1

def test_max_sub_array_sum():
    arr = [2, 4, 8, -1, 8, 4, 3, 34, -32]
    expected_result = 62
    assert max_sub_array_sum(arr) == expected_result

def test_missing_number():
    arr = [2, 3, 5, 4, 1, 8, 7]
    assert missing_number(arr) == 6
