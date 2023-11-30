#!/usr/bin/python3
"""ALX-Interview Pascal Triangle Task"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.
    """
    if n <= 0:
        return []

    triangle = [[1] * (i + 1) for i in range(n)]

    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle


if __name__ == "__main__":
    pascal_result = pascal_triangle(5)
    for row in pascal_result:
        print(row)
