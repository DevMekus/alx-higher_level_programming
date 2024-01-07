#!/usr/bin/python3

"""Matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function that return the multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Return:
        New matrix
    """

    return (np.matmul(m_a, m_b))
