import sys

line = str(sys.argv[1])
line = line.split(",")
line = [int(x) for x in line]

from collections import deque

queue = deque(line)
res = []
first = queue.popleft()
while len(queue):
	el = queue.popleft()
	res.append(el)
	if el >= first:
		first = el
		queue2 = queue
		queue = deque() 
		for ell in queue2:
			if ell > first:
				res.append(ell)
				first = ell


print(len(res))
		
#python3 viewrange.py "6,3,2,9,1,2,1,3"		
#python3 viewrange.py "8,6,7,8,10,5,12,9"