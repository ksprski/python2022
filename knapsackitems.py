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


def knapsack_items(v, w, W):
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
    
	value = sack[l-1][W]
	print(value) 
	items = []
	for i in range(l-1, 0, -1):
		if value == 0:
			break
		if value != sack[i - 1][W]:
			items.append([v[i], w[i]])
			value = value - v[i]
			W = W - w[i]
	print(items)

knapsack_items(v,w,W)         
   
#python3 knapsackitems.py "items.txt" 50 100