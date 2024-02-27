import sys, random

if len(sys.argv)==1:
	n = 5
	k = 5
elif len(sys.argv)==2:
	n = int(sys.argv[1])
	k = n
else: 
	n = int(sys.argv[1])
	k = min(n, max(1, int(sys.argv[2])))

lst = list(range(n))

for i in range(n-1):
	rnd = random.randrange(i,n)
	lst[i], lst[rnd] = lst[rnd], lst[i]

print(lst[:k])	
