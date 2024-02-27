import sys, math
N = int(sys.argv[1])

def num_mult(A, n):
	for i in range(len(A)):
			for j in range(len(A[0])):
					A[i][j] = round(A[i][j] * n, 3) 
					if A[i][j] == -0.0:
						A[i][j] = 0
	return A

def prod(A, flag):
	rows = len(A)
	columns = len(A[0])
	prod = [[0]*columns*2 for i in range(rows)]
	for i in range(rows):
		for j in range(columns):
			prod[i][j*2] = A[i][j]
			if flag == 1:
				prod[i][j*2 + 1] = A[i][j]
			elif flag == -1:
				prod[i][j*2 + 1] = -A[i][j]
	return prod

def diag(N):
	dg = [[0]*N for i in range(N)]
	for i in range(N):
		dg[i][i] = 1
	return dg	

def haar(n):
	H = num_mult([[1, 1],[1, -1]], 2**(-0.5))
	step = int(math.log2(N)) - 1
	cnt = 1
	if n == 2:
		return H	
	else:
		for i in range(step):
			H = num_mult(H, 2**(-0.5))
			H = prod(H, 1)+prod(num_mult(diag(2**cnt), 2**(-0.5)), -1)
			cnt +=1
		return H	

print(haar(N))			


#python3 haar1.py 2