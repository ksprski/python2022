import sys
n = int(sys.argv[1])

set_val = set([25,50])
set_double = set([50])
for x in range(1, 21):
	set_val.add(x) 
	set_val.add(x*2) 
	set_double.add(x*2)
	set_val.add(x*3) 

result = []
for el in set_double:
	W = n - el
	for i in set_val:
		for j in set_val:
			if i + j == W:
				result.append([i,j,el])
print(result)

#python3 darts.py 155