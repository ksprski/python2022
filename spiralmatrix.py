import sys
n = int(sys.argv[1])

def spiral(matr, n, cur_n, val, rat):

	if val > n**2:
		return matr

	i = j = rat

	matr[i][j] = val
	val += 1
	j+=1

	while j < cur_n :
		matr[i][j] = val
		j += 1
		val += 1
	j -= 1
	i+= 1
	
	while i < cur_n:
		matr[i][j] = val
		val += 1
		i += 1
	i -= 1
	j -= 1

	while j >= rat:
		matr[i][j] = val
		val += 1
		j -= 1
	j += 1
	i -= 1

	while i > rat:
		matr[i][j] = val
		val += 1
		i -= 1

	spiral(matr, n, cur_n - 1, val, rat + 1)

	
matr = [[0]*n for _ in range(n)]
spiral(matr, n, n, 1, 0)
print('\n'.join('\t'.join(map(str, row)) for row in matr))

#python3 spiralmatrix.py 4

