import numpy as np
import matrixOperations as mops


def menu():
	print("*Type the number corresponding to the operation you want to perfrom *")
	print("* 1 : multiply a row with a constant                                *")
	print("* 2 : multiply a row with a constant                                *")
	print("* 3 : multiply a row with a constant                                *")


def mulRowConstant(m):
	rows = m.shape[0]
	print("Enter row from 0 to " +str(rows-1))
	row = int(input())
	print("Enter scalar")
	constant = int(input())
	m = mops.scalarMulRow(m,float(constant),row)
	return m

options = {
		"1" : mulRowConstant
	}

def set_matrix(currentLine,):
	rowList = []
	inNum = 1
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

if __name__ == "__main__":
	print("enter number of rows in matrix")
	inNum = int(input())
	currentLine = 1
	matrix = None 
	rowList = []
	previousMatrix = None
	originalMatrix = None

	matrix = set_matrix(currentLine)
	matrix = matrix.astype('float64')
	originalMatrix = matrix.copy()
	print("the matrix is:")
	print(matrix)
	print("\n")

	inNum = 0
	while inNum != "-1":
		func = options.get(inNum)
		if func != None:
			matrix = func(matrix)
			print(matrix)
		menu()
		inNum = input()


	
