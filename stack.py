import time, random

t1 = time.time()

def create_stack():
	stack = []
	return stack

def push(stack, item):
	stack.append(item)

def pop(stack):
	if is_empty(stack):
		return "error"
	else:
		return stack.pop()		

def peek(stack):
	if is_empty(stack):
		return "error"
	else:
		return stack[-1]	

def is_empty(stack):
	return len(stack) == 0


stack = create_stack()
for i in range(100000):
	push(stack, random.random())
for i in range(100000):
	pop(stack)

l = len(stack)
t2 = time.time()
t = t2-t1
print(t, len(stack))					


#python3 stack.py