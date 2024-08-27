from typing import List

def selection_sort(arr):
    n = len(arr)
    for i in range(n):         #first element is considered 
        min = i                #location is considered here as i have value of location 
        for j in range(i+1,n): #loop goes from i+1 till n one by one 
            if(arr[j]<arr[min]):
                min = j        #if i j < i then current min is changed from i to j 
        arr[i],arr[min] = arr[min],arr[i]
    print(arr)
    
arr = [12,89,55,9,10,6]     
selection_sort(arr)        
    