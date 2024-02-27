import sys, random, time
n = int(sys.argv[1])
m = int(sys.argv[2])
k = int(sys.argv[3])
t1 = time.time()
def merge_sort(arr, left, right):
        def merge(arr, left, right, mid):
                i = 0
                j = 0
                lst1 = arr[left:mid+1]
                lst2 = arr[mid+1:right+1]
                while i < len(lst1) and j < len(lst2):
                        if lst1[i] < lst2[j]:
                                arr[left] = lst1[i]
                                i += 1
                        else:
                                arr[left] = lst2[j]
                                j += 1
                        left += 1   
                for x in lst1[i:]:
                        arr[left] = x
                        left += 1
                for y in lst2[j:]:
                        arr[left] = y
                        left += 1
                return arr

        if (left < right):
                mid = left + (right - left) // 2
                merge_sort(arr, left, mid)
                merge_sort(arr, mid + 1, right)
                merge(arr, left, right, mid)
        return arr


numbers= []
for i in range(n):
                numbers.append(random.randrange(1, m+1))
               
output = merge_sort(numbers, 0, len(numbers) - 1)
t2 = time.time()
t = t2 - t1
if k == 0:
        print(t)
else:
        print(t, output[-k:])


#python3 mergesort.py 10 50 5   
#python3 mergesort.py 1000 600 4  
#python3 mergesort.py 10000 100000 0
