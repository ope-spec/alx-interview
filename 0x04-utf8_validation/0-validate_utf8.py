#!/usr/bin/python3
"""Module for validating UTF-8 encoding"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    def is_start_byte(byte):
        return (byte & 0b10000000) == 0b00000000

    def count_leading_ones(byte):
        count = 0
        while (byte & 0b10000000) == 0b10000000:
            count += 1
            byte <<= 1
        return count

    i = 0
    while i < len(data):
        leading_ones = count_leading_ones(data[i])

        if leading_ones == 1 or leading_ones > 4:
            return False

        for j in range(1, leading_ones):
            if i + j >= len(data) or not is_start_byte(data[i + j]):
                return False

        i += leading_ones

    return True
