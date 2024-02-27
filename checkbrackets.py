import sys

line = str(sys.argv[1])

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
flag = 0
for x in line:
	if x == "(":
		push(stack, x)
	elif x == ")":
		if not is_empty(stack):
			pop(stack)
		else:
			flag = 1
			break	
	else:
		flag = 1
		break

if flag == 1 or len(stack) > 0:
	print("False")
else:
	print("True")					

#python3 checkbrackets.py "(())()()"
#python3 checkbrackets.py "(())()(()"
#python3 checkbrackets.py "(()())())"