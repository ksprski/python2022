import sys
from collections import deque

file_name = sys.argv[1]
start = tuple([int(x) for x in sys.argv[2].split(",")])
end = tuple([int(x) for x in sys.argv[3].split(",")])

matr = []
f = open(file_name, "r", encoding="utf-8")
while True:
	s = f.readline().strip("\n")
	if s == "":
		break
	else:
		lst = [x for x in str(s)]
		matr.append(lst)
f.close()

field = []
for i in range(len(matr)):
    field.append([])
    for j in range(len(matr[0])):
        field[i].append(0)
i, j = start
field[i][j] = 1

def step(n):
	h = len(matr)
	w = len(matr[0])
	for i in range(h):
		for j in range(w):
			if field[i][j] == n - 1:
				if i - 1 >= 0 and field[i-1][j] == 0 and matr[i-1][j] == " ":
					field[i-1][j] = n
				if j - 1 >= 0 and field[i][j-1] == 0 and matr[i][j-1] == " ":
					field[i][j-1] = n
				if i + 1 < h  and field[i+1][j] == 0 and matr[i+1][j] == " ":
					field[i+1][j] = n
				if j + 1 < w  and field[i][j+1] == 0 and matr[i][j+1] == " ":
					field[i][j+1] = n
	return None	           

num = 2
i, j = end
while True:
	step(num)
	num += 1
	if field[i][j] != 0:
		break

def bfs(i, j, k):
	h = len(matr)
	w = len(matr[0])
	vertices = deque([(i,j)])
	visited = [(i,j)]
	while vertices:
		vertex = vertices.popleft()
		i, j = vertex[0], vertex[1]
		neighbors = []
		if i+1 < h and k > 1:
			if field[i+1][j] == k-1:
				neighbors.append((i+1,j))
				k -= 1
		if i-1 >= 0 and k > 1:		
			if field[i-1][j] == k-1:
				neighbors.append((i-1,j))
				k -= 1
		if j+1 < w and k > 1:		
			if field[i][j+1] == k-1:
				neighbors.append((i,j+1))
				k -= 1
		if j-1 >= 0 and k > 1:		
			if field[i][j-1] == k - 1:
				neighbors.append((i,j-1))
				k-=1
		for neighbor in neighbors:
			if neighbor not in visited:
				visited.append(neighbor)
				vertices.append(neighbor)
	visited.reverse()						
	return visited

h = len(field)
w = len(field[0])

for i in field:
	print(" ".join([str(l).rjust(2) for l in i]))
print("\n")  
i, j = end
k = field[i][j]
print(bfs(i,j, k))
#python3 pathfinder.py "maze2.txt" "1,1" "5,1"