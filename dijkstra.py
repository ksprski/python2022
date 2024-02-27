import sys
from collections import deque

file_name = sys.argv[1]
name1 = sys.argv[2]

graph = dict()
f = open(file_name, "r", encoding="utf-8")
while True:
	s = f.readline().strip("\n")
	if s == "":
		break
	else:
		city1, city2, dist = [x for x in s.split("\t")]
		dist = int(dist)
		if city1 not in graph:
			graph[city1] = dict()
			graph[city1][city2] = dist
		else:
			graph[city1][city2] = dist	
		if city2 not in graph:
			graph[city2] = dict()
			graph[city2][city1] = dist
		else:
			graph[city2][city1] = dist		
f.close()
from math import inf

dists = {x : inf for x in graph}
dists[name1] = 0

visited = dict()
vertex = name1
while dists:
	for neighbour, dist in graph[vertex].items():
		if neighbour not in visited:
			calc_dist = dists[vertex] + dist
			if dists[neighbour] > calc_dist:
				dists[neighbour] = calc_dist
	visited[vertex] = dists[vertex]
	dists.pop(vertex)
	if dists:
		next_vertex = [dist for dist in dists.items()]
		next_vertex = sorted(next_vertex,  key = lambda x: x[1])
		vertex = next_vertex[0][0]

tmp= list(visited)
print("Top 5 nearest cities:")
for i in range(1, 6):
	print(f"{tmp[i], visited[tmp[i]]}")
print("Top 5 distant cities:")
for i in range(5, 0, -1):
	print(f"{tmp[-i], visited[tmp[-i]]}")

#python3 dijkstra.py "belarus.tsv" "Минск"		