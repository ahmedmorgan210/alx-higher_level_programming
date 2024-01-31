#!/usr/bin/python3
"""matrix multiplication"""


def check_type(value, expected_type, error_message):
    """matrix multiplication"""

    if type(value) is not expected_type:
        raise TypeError(error_message)


def check_list_of_lists(value, error_message):
    """matrix multiplication"""
    if type(value) is not list:
        raise TypeError(error_message)
    for sub_value in value:
        if type(sub_value) is not list:
            raise TypeError(error_message)


def check_not_empty(value, error_message):
    if len(value) == 0 or len(value[0]) == 0:
        raise ValueError(error_message)


def check_same_size(value, error_message):
    for sub_value in value:
        if len(sub_value) != len(value[0]):
            raise TypeError(error_message)


def check_numeric(value, error_message):
    for sub_value in value:
        if type(sub_value) is not int and type(sub_value) is not float:
            raise TypeError(error_message)


def matrix_mul(m_a=[[1]], m_b=[[1]]):
    check_type(m_a, list, "m_a must be a list")
    check_type(m_b, list, "m_b must be a list")
    check_list_of_lists(m_a, "m_a must be a list of lists")
    check_list_of_lists(m_b, "m_b must be a list of lists")
    check_not_empty(m_a, "m_a can't be empty")
    check_not_empty(m_b, "m_b can't be empty")
    check_same_size(m_a, "each row of m_a must be of the same size")
    check_same_size(m_b, "each row of m_b must be of the same size")
    check_numeric(m_a, "m_a should contain only integers or floats")
    check_numeric(m_b, "m_b should contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for idx_r in range(len(result)):
        for idx_c in range(len(result[0])):
            idx_cc = 0
            for r_a in m_a[idx_r]:
                result[idx_r][idx_c] += r_a * m_b[idx_cc][idx_c]
                idx_cc += 1
    return result
