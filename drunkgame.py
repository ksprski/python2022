import sys
from collections import deque

def create_queue():
	queue = deque()
	return queue

def enqueue(queue, item):
	queue.append(item)

def dequeue(queue):
	if is_empty(queue):
		return "error"
	else:
		return queue.popleft()		

def peek(queue):
	if is_empty(queue):
		return "error"
	else:
		return queue[0]	

def is_empty(queue):
	return len(queue) == 0

def game_show(p1,p2):
	str1 = ""
	str2 = ""
	for i in first:
		str1 = str1 + str(i) + " "
	for j in second:
		str2 = str2 + str(j) + " "
	
	if (not str1) and (not str2):
		print("Все карты равны!")
	else:
		print("p1: "+str1)	
		print("p2: "+str2+"\n") 

def game(p1,p2):
	while len(p1) and len(p2):
		c1 = int(dequeue(p1))
		c2 = int(dequeue(p2))
		if c1 > c2:
			enqueue(p1, c1)
			enqueue(p1, c2)
		elif c2 > c1:
			enqueue(p2, c2)
			enqueue(p2, c1)
		elif c1 == c2:
			tmp = str(c1)+str(c2)
			while c1 == c2 and (len(p1) and len(p2)):
				c1 = dequeue(p1)
				c2 = dequeue(p2)
				if c1 >= c2:
					tmp += str(c1)
					tmp += str(c2)
				elif c2 > c1:
					tmp += str(c2)
					tmp += str(c1)	
				if c1 > c2:			
					for i in tmp:
						enqueue(p1, i) 
				elif c2 > c1:
					for j in tmp:
						enqueue(p2, j) 
		game_show(first,second)


inp = str(sys.argv[1]) + " "
l_str = len(inp)
l_kol = l_str // 2

first = create_queue()
second = create_queue()

for i in range(l_kol):
	if inp[i] != " ":
		enqueue(first, int(inp[i]))
		enqueue(second, int(inp[i + l_kol]))

game_show(first, second)
game(first, second)


#python3 drunkgame.py "2 8 4 6 1 5 3 8 3 7 4 7 6 2 1 5"
#python3 drunkgame.py "2 3 4 9 2 7 4 5"
#python3 drunkgame.py "2 2 2 4 2 2 2 2"