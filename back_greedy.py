v = [1, 3, 2, 5, 6]
w = [2, 3, 2, 5, 6]

W = 7


v1 = [ 20, 5, 10, 25, 15, 40]
W1 = 10
w1 = [ 1, 2, 3, 4, 7, 8 ]

def greedy(v,w,W):
	ratio = []
	for i in range(len(v)):
		ratio.append((v[i]/w[i], i))
	ratio = sorted(ratio, key = lambda x: x[0], reverse = True)
	take_v = 0
	take_w = 0
	for i in range(len(ratio)):
		ind = ratio[0][1]
		if (take_w + w[ind]) <= W:
			take_w += w[ind]
			take_v += v[ind]
		if take_w == W:
			break
		ratio.pop(0)	
	return take_w, take_v	

print(greedy(v,w,W))
print(greedy(v1,w1,W1))						

def greedy1(v,w,W):
	items = [[v[i]/w[i], v[i], w[i]] for i in range(len(v))]
	items = sorted(items, reverse = True)
	knapsack = {"value": 0, "weight": 0, "items": []}
	for item in items:
		_, value, weight = item	
		if knapsack["weight"] + weight <= W:
			knapsack["value"] += value
			knapsack["weight"] += weight
			knapsack["items"].append([value, weight])
		if 	knapsack["weight"] == W:
			break
		return knapsack	

print(greedy1(v,w,W))
print(greedy1(v1,w1,W1))						