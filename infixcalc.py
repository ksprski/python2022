import sys
pol = str(sys.argv[1])
pol = pol.split(" ")

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

def top(stack):
	if is_empty(stack):
		return "error"
	else:
		return stack[-1]	

def is_empty(stack):
	return len(stack) == 0

def dijkstra(line):
	prior = {"*":3, "/":3, "+":2, "-":2, "(":1}
	operations = ["+","-","/","*"]
	stck = create_stack()
	op_stck = create_stack()
	for ch in line:
		if ch in operations:
			while (not is_empty(op_stck)) and (prior[top(op_stck)] >= prior[ch]):
				push(stck, pop(op_stck))
			push(op_stck, ch)	
		elif ch == "(":
			push(op_stck, ch)
		elif ch == ")":
			cur = pop(op_stck)
			while cur != "(":
				push(stck, cur)
				cur = pop(op_stck)
		else:
			push(stck, ch)	
	while not is_empty(op_stck):
		push(stck, pop(op_stck))
	return stck		


def calc(x, y, op):
	if op == "+":
		return x + y
	elif op == "-":
		return x - y
	elif op == "*":
		return x*y
	elif op == "/":
		return x/y			

def check(line):
	check = True
	oprtns = ["+","-","/","*"]
	for i in range(len(line) - 2):	
		if (line[i] in oprtns) and (line[i + 1] in oprtns):
			return False
	oprtns2 = ["+","-","/","*", ")", "("]		
	for i in range(len(line) - 2):	
		if line[i] not in oprtns2 and line[i+1] not in oprtns2:
			return False	
	return check


stack = create_stack()

oprtns = ["+","-","/","*"]



flag = 0
try:
	if check(pol):
		pol = dijkstra(pol)
		for x in pol:
			if x in oprtns:
				if not is_empty(stack):
					b = pop(stack)
					if not is_empty(stack):
						a = pop(stack)
						push(stack, calc(a, b, x))
					else:
						print("invalid input")
						flag = 1
						break
				else:
					print("invalid input")		
					flag = 1
					break	
			else:
				push(stack, int(x))
		if len(stack) == 1:
			print(stack[0])	
		elif len(stack) != 1 and not flag:
			print("invalid input")		
			flag = 1
	else:
		print("invalid input")		
		flag = 1					
except ValueError:
	if flag == 0:
		print("invalid input")
	flag = 1	
except IndexError:
	if flag == 0:
		print("invalid input")


#python3 infixcalc.py "4 + 3 * 2"
#python3 infixcalc.py "( 3 + 9 ) / 2 * 5 - ( 15 - 10 ) / 5"
#python3 infixcalc.py "3 + 9 -"
#python3 infixcalc.py "( 22 + 10 ) / 2 + 11 - 3 * 10" 
#python3 infixcalc.py "3 9 -"