import sys

def merge_sort(arr, left, right):
	def merge(str1, str2):
		result = ""
		i = 1
		j = 1
		while i <= len(str1) and j <= len(str2):
			if str1[-i] == str2[-j]:
				result += str1[-i]
			else:
				break
			i += 1
			j += 1	
		return result[::-1]

	if left < right:
		mid = left + (right - left) // 2
		str1 = merge_sort(arr, left, mid)
		str2 = merge_sort(arr, mid + 1, right)
		arr = merge(str1, str2)
	elif left == right:
		arr = arr[left]	
	return arr     

words = str(sys.argv[1]).split(" ")

l = len(words)
result = merge_sort(words, 0, l - 1)
if len(result):
    print(result)
else:
    print(" ")
 

#python3 mergepostfix.py "starlink hyperlink weblink" 
#python3 mergepostfix.py "starlink hyperlink weblink eink ink" 
#python3 mergepostfix.py "starlink hyperlink weblink bing" 