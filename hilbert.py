import sys
import matplotlib.pyplot as plt

n = int(sys.argv[1])

def matr_mult(A,B):
	C = [0,0] 
	for i in range(len(A)):
		for j in range(len(B[0])):
			s = 0
			for k in range(len(B)):
				s += A[k]*B[k][j]
				C[j] = s
	return C

R1 = [[0,-1],[1,0]]
R2 = [[0,1],[-1,0]]

def rplc(n, way):
	newway = ""
	for ch in way:
		if ch == "L":
			newway += "+RF-LFL-FR+"
		elif ch == "R":	
			newway += "-LF+RFR+FL-"
		elif ch == "+" or ch =="-" or ch == "F":
			newway += ch
	way = newway		
	n -= 1
	if n <= 0:
		return way
	else:	
		return rplc(n, way)

way = "L"
way = rplc(n, way)

matrix = [[0,0]]
vect = [1,0]
for i in way:
	if i == "+":
		vect = matr_mult(vect, R2)

	elif i == "-":
		vect = matr_mult(vect, R1)

	elif i == "F":
		matrix.append([matrix[-1][0]+vect[0], matrix[-1][1]+vect[1]]) 

matrix = [*zip(*matrix)]
plt.plot(matrix[0], matrix[1], "k")
plt.axis('equal');
plt.show()


#python3 hilbert.py 7	