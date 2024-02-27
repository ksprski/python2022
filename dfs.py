import sys
from collections import deque

file_name = sys.argv[1]
start_vert = sys.argv[2]


def dfs(graph, start, visited = 0):
	if not visited: 
		visited = set([start])
	else: 
		visited.add(start)
	for neighbor in graph[start]:
		if neighbor not in visited:
			dfs(graph, neighbor, visited)
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
print(dfs(graph, start_vert))		

#python3 dfs.py "cities.tsv" "Полоцк"