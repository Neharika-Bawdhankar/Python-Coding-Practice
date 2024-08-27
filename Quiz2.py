# Write a Python program that takes a list of numbers and counts how many of them are even and how many are odd.

def Check_Numbers(NumList):
    n = len(NumList)
    even_count = 0 
    odd_count = 0
    for i in range(n):   
        if(NumList[i]%2 == 0):
            even_count += 1
        else:
            odd_count += 1
    print("Even:", even_count, "Odd:", odd_count)
    return even_count,odd_count
    
    
NumList = [12,9,41,22,10,5,21]
Check_Numbers(NumList)