import numpy as np

def scalar_mul_row(matrix,scalar,R):
    resM = matrix.copy()
    resM[R] = resM[R]*scalar
    print("row ",R," multiplied by ",scalar)
    return resM

def interchange(matrix,R1,R2):
    print("hello")
    Mcopy = np.array(matrix)
    matrix[R1] = matrix[R2]
    matrix[R2] = Mcopy[R1]
    print("row ",R1," swapped with ",R2)
    return matrix

def add_scalar_times_row(matrix,scalar,constRow,affectedRow):
    conM = np.array(matrix)
    resM = np.array(matrix)
    rowForAddition = conM[constRow] * scalar
    resM[affectedRow] = resM[affectedRow] + rowForAddition
    print("row: ",constRow," multiplied by ", scalar, " added to the ", affectedRow, "row")
    return resM

if __name__ == "__main__":
    matrix = np.ones((2,2))
    matrix = scalar_mul_row(matrix,1,3)
    matrix = interchange(matrix,0,1)
    print(matrix)
    matrix = add_scalar_times_row(matrix,3,0,1)
    print(matrix)
