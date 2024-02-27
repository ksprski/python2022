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
		city1 , city2, dist = [x for x in s.split("\t")]
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
n = len(graph)
for i in range(n-1):
	for vertex in graph:
		for neighbour in graph[vertex]:
			if dists[vertex] + graph[vertex][neighbour] < dists[neighbour]:
				dists[neighbour] = dists[vertex] + graph[vertex][neighbour]

sorted_dists = {}
sorted_keys = sorted(dists, key=dists.get)
for i in sorted_keys:
    sorted_dists[i] = dists[i]		
tmp = list(sorted_dists)

print("Top 5 nearest cities:")
for i in range(1, 6):
	print(f"{tmp[i], dists[tmp[i]]}")
print("Top 5 distant cities:")
for i in range(5, 0, -1):
	print(f"{tmp[-i], dists[tmp[-i]]}")

#python3 bellman.py "belarus.tsv" "Минск"		