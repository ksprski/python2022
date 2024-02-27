from collections import deque
import time, random

t1 = time.time()

def create_queue():
	queue = deque()
	return queue

def enqueue(queue, item):
	queue.appendleft(item)

def dequeue(queue):
	if is_empty(queue):
		return "error"
	else:
		return queue.pop()		

def peek(queue):
	if is_empty(queue):
		return "error"
	else:
		return queue[0]	

def is_empty(queue):
	return len(queue) == 0
				

queue = create_queue()
for i in range(100000):
	enqueue(queue, random.random())
for i in range(100000):
	dequeue(queue)

l = len(queue)
t2 = time.time()
t = t2-t1
print(t, l)	


#python3 queue.py