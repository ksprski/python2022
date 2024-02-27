from collections import deque
def bfs_dist(graph, start):
	vertices = deque([start])
	visited = set([start])
	distances = {x : -1 for x in graph.keys()}
	while vertices:
		vertex = vertices.popleft()
		if vertex == start:
			distances[vertex] = 0
		for neighbor in graph[vertex]:
			if neighbor not in visited:
				distances[neighbor] = distances[vertex] + 1
				visited.add(neighbor)
				vertices.append(neighbor)
	return distances

graph = {
	1: {2, 3},
	2: {1,3},
	3: {1,2,4,5},
	4: {3},
	5: {3},

}	

print(bfs_dist(graph, 5))