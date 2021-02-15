import numpy as np




if __name__ == "__main__":
	print("enter number of rows in matrix")
	s = int(input())
	currentLine = 1
	matrix = None 
	while s > 0:
		print("please enter row" +str(currentLine) +"of a matrix, seperate with \',\'")
		m_in = input()
		sSplit = m_in.split(',')
		for n in sSplit:
			n = float(n)
		if currentLine == 1:
			matrix = np.array(sSplit)
		else:
			m = np.array(sSplit)
			matrix = np.stack((matrix,m))
		currentLine += 1
		s -= 1

	print(matrix)
