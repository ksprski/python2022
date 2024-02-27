import sys, random
n = int(sys.argv[1])

lst1 = []
len1 = random.randrange(1, n+1)
lst2 = []
len2 = random.randrange(1, n+1)
len3 = max(len1,len2)
len4 = min(len1, len2)
for i in range(len4):
		lst1.append(random.randrange(0, n+1))
		lst2.append(random.randrange(0, n+1))
lst = random.choice([lst1,lst2])
for j in range(len3 - len4):
	lst.append(random.randrange(0, n+1))

lst1 = sorted(lst1)
lst2 = sorted(lst2)		
print(lst1)
print(lst2)

i = 0
j = 0
lst3 = []
while i < len(lst1) and j < len(lst2):
	if lst1[i] < lst2[j]:
		lst3.append(lst1[i])
		i += 1
	else:
		lst3.append(lst2[j])
		j += 1
lst3 += lst1[i:]
lst3 += lst2[j:] 
   
print(lst3)

#python3 mergelists.py 20			