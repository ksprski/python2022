import sys
from collections import deque

file_name = sys.argv[1]
start_vert = sys.argv[2]


def bfs(graph, start):
	vertices = deque([start])
	visited = set([start])
	while vertices:
		vertex = vertices.popleft()
		for neighbor in graph[vertex]:
			if neighbor not in visited:
				visited.add(neighbor)
				vertices.append(neighbor)
	return visited


graph = {}
f = open(file_name, "r", encoding="utf-8")
while True:
	s = f.readline().strip("\n")
	if s == "":
		break
	else:
		city1 , city2 = [x for x in s.split("\t")]
		if city1 not in graph:
			graph[city1] = set([city2])
		else:
			graph[city1].add(city2)	
		if city2 not in graph:
			graph[city2] = set([city1])
		else:
			graph[city2].add(city1)		

f.close()
print(bfs(graph, start_vert))		

#python3 bfs.py "cities.tsv" "Полоцк"
#python3 bfs.py "graph.tsv" "9"