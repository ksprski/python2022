import sys, math
size = int(sys.argv[1])

h = [[0]*size for i in range(size)]
h[0][0] = 1
l = int(math.log2(size))

for m in range(l):
	for i in range(2**m):
		for j in range(2**m):
			h[i][j+2**m] = h[i][j]
			h[i+2**m][j] = h[i][j]
			h[i+2**m][j+2**m] = -h[i][j]
		

t = [[0] * size for i in range(size)]
for i in range(size):
        for j in range(size):
                t[i][j] = h[j][i]


p = [[0] * size for i in range(size)]
for i in range(size):
        for j in range(size):
                for k in range(size):
                        p[i][j] += h[i][k] * t[k][j]




for i in range(size):
	s = ''
	for j in range(size):
		s += str(h[i][j]) + '\t'

	print(s,'\n','\n')

for i in range(size):
	y = ''
	for j in range(size):
		y += str(t[i][j]) + '\t'

	print(y,'\n')

for i in range(size):
	u = ''
	for j in range(size):
		u += str(p[i][j]) + '\t'

	print(u)
