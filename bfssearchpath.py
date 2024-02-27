import sys
from collections import deque

file_name = sys.argv[1]
name1 = sys.argv[2]
name2 = sys.argv[3]


def bfs_dist(graph, start, end):
	flag = 0
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
		print(f"Distance: {distances[end]}")
	else:
		print("No connection")
		flag = 1
	return flag	

def search_path(graph, start, end):
	vertices = deque([(start,[start])])
	visited = set([start])
	while vertices:
		vertex, path = vertices.popleft()
		for neighbor in graph[vertex]:
			if neighbor == end:
				return path + [end]
			else:
				if neighbor not in visited:
					visited.add(neighbor)
					vertices.append((neighbor, path + [neighbor]))                   

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


flag = bfs_dist(graph, name1, name2)
path = search_path(graph, name1, name2)
if flag == 0:
	for i in range(len(path) - 1):
		movie = set(actors[path[i]]) & set(actors[path[i+1]])
		print(f"{path[i]} was with {path[i + 1]} in {movie}")

#python3 bfssearchpath.py "actors.tsv" "Kevin Bacon" "Tom Hanks"
#bfssearchpath.py "actors.tsv" "Kevin Bacon" "Tom Hardy"