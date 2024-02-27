import sys, random, copy, time

if len(sys.argv) == 3:
        n = int(sys.argv[1])
        if sys.argv[2] == "True":
                out = True
        else:
                out = False        

elif len(sys.argv) == 2:
        n = int(sys.argv[1])
        out = False
else:
        n = 10
        out = False

numbers = [random.randint(0,1000) for _ in range(n)]


def python_sort(lst, out):
        print('\npython sort')        
        arr = copy.deepcopy(lst)         
        t0 = time.time()                 
        arr.sort()                                
        print(time.time() - t0)        
        if out:                                
                print(arr)


def bubble_sort(lst, out):
        print('\nbuble sort')       
        arr = copy.deepcopy(lst)         
        t0 = time.time()                 
        
        flag = True
        i = 1
        while flag:
                flag = False
                for j in range(n - i):
                        if arr[j] > arr[j + 1]:
                                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                                flag = True 
                i += 1

        print(time.time() - t0)        
        if out:                                
                print(arr)

def insertion_sort(lst, out):
        print('\ninsertion sort')        
        arr = copy.deepcopy(lst)         
        t0 = time.time()                 

        for i in range(1, n):
                key = arr[i]
                j = i - 1
                while j >= 0 and arr[j] > key:
                        arr[j + 1] = arr[j]
                        j -= 1
                arr[j + 1] = key        

        print(time.time() - t0)        
        if out:                                
                print(arr)

def selection_sort(lst, out):
        print('\nselection sort')        
        arr = copy.deepcopy(lst)         
        t0 = time.time()                

        for i in range(n - 1):
                minindex = i
                for j in range(i + 1, n):
                        if arr[j] < arr[minindex]:
                                minindex = j    
                if minindex != i:
                        arr[i], arr[minindex] = arr[minindex], arr[i]

        print(time.time() - t0)        
        if out:                                
                print(arr)


def quick_sort(lst, out):
        def quicksort(nums, fst, lst):
                if fst >= lst: 
                        return None
 
                i, j = fst, lst
                p = nums[(fst + lst)//2]
                 
                while i <= j:
                        while nums[i] < p: 
                                i += 1
                        while nums[j] > p: 
                                j -= 1
                        if i <= j:
                                nums[i], nums[j] = nums[j], nums[i]
                                i, j = i + 1, j - 1
                quicksort(nums, fst, j)
                quicksort(nums, i, lst)


        print('\nquick sort')        
        arr = copy.deepcopy(lst)         
        t0 = time.time() 
        quicksort(arr, 0, n - 1)
        print(time.time() - t0)        
        if out:                                
                print(arr)        
        

def merge_sort(lst, out):
        def mergesort(arr, left, right):
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
                        mergesort(arr, left, mid)
                        mergesort(arr, mid + 1, right)
                        merge(arr, left, right, mid)
                return arr

        print('\nmerge sort')        
        arr = copy.deepcopy(lst)         
        t0 = time.time() 
        mergesort(arr, 0, n - 1)
        print(time.time() - t0)        
        if out:                                
                print(arr)        
        
bubble_sort(numbers, out)
insertion_sort(numbers, out)
selection_sort(numbers, out)
quick_sort(numbers, out)
merge_sort(numbers, out)
python_sort(numbers, out)