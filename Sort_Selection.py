from typing import List

def selectionsort(arr: List[int])-> None:
    n = len(arr)
    #print(n)
    for i in range(n):
        #print(i)
        min = i
        for j in range(i+1,n):
            #print(j)
            if arr[j]<min:
                min = j
        arr[min],arr[i] = arr[i],arr[min]        
                
            
selectionsort(arr = [13,46,24,52,20,9])