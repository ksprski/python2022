import sys
from collections import deque

file_name = sys.argv[1]

def bfs(i, j):
	h = len(matr)
	w = len(matr[0])
	
	vertices = deque([(i,j)])
	visited = set([(i,j)])
	while vertices:
		vertex = vertices.popleft()
		i, j = vertex[0], vertex[1]
		neighbors = []
		if i+1 < h:
			if matr[i+1][j] != " ":
				neighbors.append((i+1,j))
		if i-1 >= 0:		
			if matr[i-1][j] != " ":
				neighbors.append((i-1,j))
		if j+1 < w:		
			if matr[i][j+1] != " ":
				neighbors.append((i,j+1))
		if j-1 >= 0:		
			if matr[i][j-1] != " ":
				neighbors.append((i,j-1))
		for neighbor in neighbors:
			if neighbor not in visited:
				visited.add(neighbor)
				vertices.append(neighbor)			
	return visited


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

h = len(matr)
w = len(matr[0])

print(len(bfs(h//2, w//2)))		
#python3 findarea.py "area1.txt"		
#python3 findarea.py "area2.txt"
