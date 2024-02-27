import sys
line = str(sys.argv[1])

def rvrs(line):
	if line:
		return line[-1] + rvrs(line[:-1])
	else:
		return line
	
print(line == rvrs(line))

#python3 palindrome.py "1234321"
#python3 palindrome.py "12343210"
