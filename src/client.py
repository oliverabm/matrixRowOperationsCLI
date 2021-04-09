import numpy as np
import matrixOperations as mops


def _menu():
	print("* Type the number corresponding to the operation you want to perfrom *")
	print("* 1 : Multiply a row with a num                                      *")
	print("* 2 : interchange two rows                                           *")
	print("* 3 : Add a num times one row to another                             *")
	print("*-1 : Exit                                                           *")


def _mul_row_num(m):
	rows = m.shape[0]
	print("Enter row from 0 to " +str(rows-1))
	row = int(input())
	print("Enter num")
	num = int(input())
	print("row ",row," multiplied by ",num)
	m = mops.num_mul_row(m,float(num),row)
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

def _add_num_times_row(m):
	rows = m.shape[0]
	print("Enter row (R1) from 0 to " +str(rows-1))
	row1 = int(input())
	print("Enter num to multiply R1 by")
	num = int(input())
	print("Enter row (R2) from 0 to " +str(rows-1))
	row2 = int(input())
	print("row: ",row1," multiplied by ", num, " added to the ", row2, "row")
	m = mops.add_num_times_row(m,num,row1,row2)
	return m


def _create_matrix():
	print("enter number of rows in matrix (confirm with ENTER)")
	inNum = int(input())
	currentLine = 1
	rowList = []
	while inNum > 0:
		print("please enter row " +str(currentLine-1) +" of the matrix, seperate with \',\'")
		m_in = input()
		sSplit = m_in.split(',')
		for n in sSplit:
			n = float(n)
		rowList.append(np.array(sSplit))

		currentLine += 1
		inNum -= 1
	return np.stack(rowList)

options = {
		"1" : _mul_row_num,
		"2" : _interchange,
		"3" : _add_num_times_row
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


	
