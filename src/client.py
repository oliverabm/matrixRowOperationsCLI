import numpy as np
import matrixOperations as mops


def _menu():
	print("* Type the number corresponding to the operation you want to perfrom *")
	print("* 1 : Multiply a row with a scalar                                   *")
	print("* 2 : interchange two rows                                           *")
	print("* 3 : Add a scalar times one row to another                          *")
	print("*-1 : Exit                                                           *")


def _mul_row_scalar(m):
	rows = m.shape[0]
	print("Enter row from 0 to " +str(rows-1))
	row = int(input())
	print("Enter scalar")
	scalar = int(input())
	print("row ",row," multiplied by ",scalar)
	m = mops.scalar_mul_row(m,float(scalar),row)
	return m

def _interchange(m):
	rows = m.shape[0]
	print("Enter first row from 0 to " +str(rows-1))
	row1 = int(input())
	print("Enter second row from 0 to " +str(rows-1))
	row2 =  int(input())
	print("row ",row1," swapped with ",row2)
	m = mops.interchange(m,row1,row2)
	return m

def _add_scalar_times_row(m):
	rows = m.shape[0]
	print("Enter row (R1) from 0 to " +str(rows-1))
	row1 = int(input())
	print("Enter scalar to multiply R1 by")
	scalar = int(input())
	print("Enter row (R2) from 0 to " +str(rows-1))
	row2 = int(input())
	print("row: ",row1," multiplied by ", scalar, " added to the ", row2, "row")
	m = mops.add_scalar_times_row(m,scalar,row1,row2)
	return m


def _create_matrix():
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
		"1" : _mul_row_scalar,
		"2" : _interchange,
		"3" : _add_scalar_times_row
	}

if __name__ == "__main__":
	matrix = None 
	previousMatrix = None
	originalMatrix = None

	matrix = _create_matrix()
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
		_menu()
		inNum = input()


	
