import sys
from collections import deque

file_name = sys.argv[1]


def bfs(graph):
	k = [x for x in graph.keys()]
	start = k[0]
	result = []
	while k:
		vertices = deque([start])
		visited = set([start])
		while vertices:
			vertex = vertices.popleft()
			for neighbor in graph[vertex]:
				if neighbor not in visited:
					visited.add(neighbor)
					vertices.append(neighbor)
		result.append(visited)
		for x in visited:
			k.remove(x)
		if k:
			start = k[0]	
	return result	


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


print(bfs(graph))	

#python3 graphparts.py "graph2.tsv"