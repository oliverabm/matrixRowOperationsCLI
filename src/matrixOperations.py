import numpy as np

def num_mul_row(matrix,num,R):
    """
        The matrix operation of multiplying a row by a number
        Returns the row R multiplied by num.
    """

    resM = matrix.copy()
    resM[R] = resM[R]*num
    return resM

def interchange(matrix,R1,R2):
    """Returns the input matrix with rows R1 and R2 swapped."""
    Mcopy = np.array(matrix)
    matrix[R1] = matrix[R2]
    matrix[R2] = Mcopy[R1]
    return matrix

def add_num_times_row(matrix,num,constRow,affectedRow):
    """Returns the matrix with constRow multiplied by num added to affectedRow."""
    conM = np.array(matrix)
    resM = np.array(matrix)
    rowForAddition = conM[constRow] * num
    resM[affectedRow] = resM[affectedRow] + rowForAddition
    return resM
