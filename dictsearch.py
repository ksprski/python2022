import sys, time

word = str(sys.argv[2])

f = open(sys.argv[1], 'r', encoding='utf8')
text = f.read()
text = text.split("\n")
f.close()   

def substr(str1, str2):
	i = j = 0
	while i < len(str1) and j < len(str2):
			if str1[i] != str2[j]:
				break
			i+=1
			j+=1
	if i == len(str1):
		return True
	else:
		return False

t1 = time.time()
lin_search = []
for item in text:
	if substr(word, item):
		lin_search.append(item)
t2 = time.time()
print(lin_search, t2-t1)


bin_search = []
flag = 0
first_ind = 0
last_ind = len(text)-1
while True:
	if text[first_ind] < text[last_ind]:
		m = int((first_ind + last_ind)//2)
		if substr(word, text[m]):
			flag = 1
			break
		elif word < text[m]:
			last_ind = m - 1
			continue
		else:
			first_ind = m + 1	
			continue
	elif first_ind == last_ind and not substr(word, text[first_ind]):
		break
	elif first_ind == last_ind and substr(word, text[first_ind]):	
		bin_search.append(text[first_ind])
		break
if flag == 1:
	l = len(text)
	tmp = m
	while substr(word, text[tmp]) and tmp >= 0:
		tmp -= 1
		if tmp == -1:
			break
	tmp += 1	
	while substr(word, text[tmp]) and tmp <= (l - 1):
		bin_search.append(text[tmp])
		tmp += 1
		if tmp == l:
			break
	
t3 = time.time()	
print(bin_search, t3-t2)


#python3 dictsearch.py "dict.txt" "virus"
#python3 dictsearch.py "dict.txt" "vyrus"
