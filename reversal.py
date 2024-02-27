import sys

line = str(sys.argv[1])
line = line.split(",")

from collections import deque

queue1 = deque(line)
queue2 = deque()
def reverse(q1, q2):
	if len(q1) == 0:
		return q2
	else:
		q2.append(q1.pop())	
		return reverse(q1, q2)


print(reverse(queue1, queue2))

#python3 reversal.py "1,2,3,4,5"	
#python3 reversal.py "11,22,3,4,55"	