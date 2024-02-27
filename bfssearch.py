import sys
from collections import deque

file_name = sys.argv[1]
name1 = sys.argv[2]
name2 = sys.argv[3]


def bfs_dist(graph, start, end):
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
		if end in vertices:
			break
	if end in vertices:
		return distances[end]
	else:
		return -1	

actors = {}
movies = {}

f = open(file_name, "r", encoding='utf8')
while True:
	s = f.readline().strip("\n")
	if s == "":
		break
	else:
		actor, movie = [x for x in s.split("	")]
		if actor not in actors:
			actors[actor] = set([movie])
		else:
			actors[actor].add(movie)
		if movie not in movies:
			movies[movie] = set([actor])
		else:
			movies[movie].add(actor)
f.close()

graph = {}

for actor in actors:
	tmp = set()
	for movie in actors[actor]:
		tmp.update(movies[movie])
	graph[actor] = tmp - set([actor])	

print(bfs_dist(graph, name1, name2))	

#python3 bfssearch.py "actors.tsv" "Kevin Bacon" "Tom Hanks"
#bfssearch.py "actors.tsv" "Kevin Bacon" "Tom Hardy"
#bfssearch.py "actors.tsv" "Ralph Fiennes" "Tom Hardy"