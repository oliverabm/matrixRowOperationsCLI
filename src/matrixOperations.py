import numpy as np

def scalar_mul_row(matrix,scalar,R):
    resM = matrix.copy()
    resM[R] = resM[R]*scalar
    return resM

def interchange(matrix,R1,R2):
    Mcopy = np.array(matrix)
    matrix[R1] = matrix[R2]
    matrix[R2] = Mcopy[R1]
    return matrix

def add_scalar_times_row(matrix,scalar,constRow,affectedRow):
    conM = np.array(matrix)
    resM = np.array(matrix)
    rowForAddition = conM[constRow] * scalar
    resM[affectedRow] = resM[affectedRow] + rowForAddition
    return resM
