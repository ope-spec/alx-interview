#!/usr/bin/python3
'''Minimum Operations python3 challenge'''


def minOperations(target_chars):
    """
    Calculates the fewest number of
    operations needed to result in exactly target_chars H
    characters in this file.
    """

    chars_in_file = 1
    copied_chars = 0
    operations_count = 0

    while chars_in_file < target_chars:
        if copied_chars == 0:
            copied_chars = chars_in_file
            operations_count += 1

        if chars_in_file == 1:
            chars_in_file += copied_chars
            operations_count += 1
            continue

        remaining = target_chars - chars_in_file

        if remaining < copied_chars:
            return 0

        if remaining % chars_in_file != 0:
            chars_in_file += copied_chars
            operations_count += 1
        else:
            copied_chars = chars_in_file
            chars_in_file += copied_chars
            operations_count += 2

    if chars_in_file == target_chars:
        return operations_count
    else:
        return 0
