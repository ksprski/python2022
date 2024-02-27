import sys

n = int(sys.argv[1])

def sum(n):

    if n < 10:
        return n
    else:
        return n%10 + sum(n//10)
        
print(sum(n))

#python3 sumdigits.py 123456789        