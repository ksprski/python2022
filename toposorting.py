import sys
from collections import deque

file_name = sys.argv[1]


graph = {}
counter = set()
f = open(file_name, "r", encoding="utf-8")
while True:
	s = f.readline().strip("\n")
	if s == "":
		break
	else:
		item1, item2 = s.split("\t")
		counter.add(item2)
		counter.add(item1)
		if item1 not in graph:
			graph[item1] = list()
			graph[item1].append(item2)
		else:
			graph[item1].append(item2)		
f.close()

visited = dict()
order = list()
l = len(counter)
curLabel = l
def dfs_topo(graph, start):
	global curLabel
	visited[start] = True
	if start in graph:
		for x in range(len(graph[start])):
			neighbor = graph[start][x]
			if neighbor not in visited:
				dfs_topo(graph, neighbor)
	order.append((start, curLabel))
	curLabel -= 1

for i in graph.keys():
	if i not in visited:
		dfs_topo(graph, i)

result = list()
for el in order:
	result.append(el[0])
print(result)
#python3 toposorting.py "graph.tsv"