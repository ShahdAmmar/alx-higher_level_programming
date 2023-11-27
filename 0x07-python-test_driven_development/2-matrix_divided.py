#!/usr/bin/python3
"""Module for matrix_divided method."""


def matrix_divided(matrix, div):
    """Divides elements of matrix by div.
    Args: matrix, div
    Returns: list of divided numbers
    Raises: TypeError, ZeroDivisionError
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")

