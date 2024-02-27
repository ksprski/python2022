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

oprtns = ["+","-","/","*"]


def calc(x, y, op):
	if op == "+":
		return x + y
	elif op == "-":
		return x - y
	elif op == "*":
		return x*y
	elif op == "/":
		return x/y			


stack = create_stack()

flag = 0
try:
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
except ValueError:
	if flag == 0:
		print("invalid input")
	flag = 1	
except IndexError:
	if flag == 0:
		print("invalid input")

			

#python3 postfixcalc.py "4 3 2 * +"
#python3 postfixcalc.py "3 9 + 2 / 5 * 15 10 - 5 / -"
#python3 postfixcalc.py "3 9 + +"
#python3 postfixcalc.py "3 9 5 - +"
