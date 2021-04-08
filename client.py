import numpy as np
import matrixOperations as mops


def menu():
	print("*Type the number corresponding to the operation you want to perfrom *")
	print("* 1 : Multiply a row with a scalar                                *")
	print("* 2 : Interchange two rows                                        *")
	print("* 3 : multiply a row with a scalar                                *")


def mul_row_scalar(m):
	rows = m.shape[0]
	print("Enter row from 0 to " +str(rows-1))
	row = int(input())
	print("Enter scalar")
	scalar = int(input())
	m = mops.scalar_mul_row(m,float(scalar),row)
	return m

def interchange(m):
	rows = m.shape[0]
	print("Enter first row from 0 to " +str(rows-1))
	row1 = int(input())
	print("Enter second row from 0 to " +str(rows-1))
	row2 =  int(input())
	m = mops.interchange(m,row1,row2)
	return m

def create_matrix():
	print("enter number of rows in matrix")
	inNum = int(input())
	currentLine = 1
	rowList = []
	while inNum > 0:
		print("please enter row" +str(currentLine) +"of a matrix, seperate with \',\'")
		m_in = input()
		sSplit = m_in.split(',')
		for n in sSplit:
			n = float(n)
		rowList.append(np.array(sSplit))

		currentLine += 1
		inNum -= 1
	return np.stack(rowList)

options = {
		"1" : mul_row_scalar,
		"2" : interchange
	}

if __name__ == "__main__":
	matrix = None 
	previousMatrix = None
	originalMatrix = None

	matrix = create_matrix()
	matrix = matrix.astype('float64')
	originalMatrix = matrix.copy()
	print("the matrix is:")
	print(matrix)
	print("\n")

	inNum = 0
	while inNum != "-1":
		func = options.get(inNum)
		if func != None:
			previousMatrix = matrix.copy()
			matrix = func(matrix)
			print(matrix)
		menu()
		inNum = input()


	
