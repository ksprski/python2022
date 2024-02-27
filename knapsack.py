import sys, time
file_name = sys.argv[1]
n = int(sys.argv[2])
W = int(sys.argv[3])

v = []
w = []
f = open(file_name, "r", encoding="utf-8")
for i in range(n):
	s = f.readline().strip("\n")
	if s == "":
		break
	else:
		val, wei = [int(x) for x in s.split("\t")]
		v.append(val)
		w.append(wei)	
f.close()

def knapsack_greedy(v,w,W):
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
	return take_v

print("Greedy knapsack")
t0 = time.time()
print(knapsack_greedy(v,w,W))
print(time.time() - t0, "\n")   	

def knapsack_recursive(v,w,i, W):
	if i == 0 or W == 0:
		return 0
	if  W - w[i-1] < 0:
		return knapsack_recursive(v, w, i - 1, W)
	else:
		return max(v[i-1] + knapsack_recursive(v, w, i - 1, W - w[i-1]), knapsack_recursive(v, w, i - 1, W))

#print("Recursive knapsack")
#t0 = time.time()
#print(knapsack_recursive(v,w,len(v), W))
#print(time.time() - t0)   		

def knapsack_topdown(v,w,i, W, lookup = dict()):
	if i == 0 or W == 0:
		return 0
	if  W - w[i-1] < 0:
		return knapsack_topdown(v, w, i - 1, W, lookup)
	if (i, W) in lookup:
		return lookup[(i, W)]
	else:
		val = max(v[i-1] + knapsack_topdown(v, w, i - 1, W - w[i-1], lookup), knapsack_topdown(v, w, i - 1, W, lookup))
		lookup[(i,W)] = val
		return val

print("Top-down knapsack")
t0 = time.time()
print(knapsack_topdown(v,w,len(v), W))
print(time.time() - t0, "\n")   

def knapsack_bottomup(v,w,W):
	sack = []
	l = len(v)
	for i in range(l):
		sack.append([])
		for j in range(W+1):
			sack[i].append(0)
	for i in range(l):
		for j in range(W+1):
			if w[i] > j:
				sack[i][j] = sack[i-1][j]
			else:
				sack[i][j] = max(v[i] + sack[i-1][j-w[i]], sack[i-1][j])
	return sack[l-1][W]
print("Bottom-up knapsack")
t0 = time.time()
print(knapsack_bottomup(v,w,W))
print(time.time() - t0)   

#python3 knapsack.py "items.txt" 50 100
	