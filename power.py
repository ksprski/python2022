import sys
a = int(sys.argv[1])
n = int(sys.argv[2])

def power(a, n):
    if n == 0:
    	return 1
    else:
    	
    	if n % 2:
    		return power(a, n - 1)*a
    	else:
    		return power(a, n / 2)*power(a, n / 2)

print(power(a, n))

#python3 power.py 3 15