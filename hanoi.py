import sys
n = int(sys.argv[1])

def hanoi(n, src, dst, aux):
	if n == 1:
		return [(src, dst)]
	else:
		return hanoi(n - 1, src, aux, dst) + [(src, dst)] + hanoi(n-1, aux, dst, src)

print(hanoi(n, 1, 2, 3))


#python3 hanoi.py 3		