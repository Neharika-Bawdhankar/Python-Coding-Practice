def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        # print("i:",arr[i])
        for j in range( i+1):
            # print("j:", arr[j])
            if(arr[i]>arr[j]):
                arr[j],arr[i] = arr[i],arr[j]
    print(arr)
                  
arr = [12,5,6,43,23,19]
bubblesort(arr)