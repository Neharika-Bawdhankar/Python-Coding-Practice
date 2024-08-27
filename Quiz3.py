# Problem 3: Find the Largest Number
# Write a Python program that finds the largest number in a given list.

def Find_Largest(Num_List):
    n = len(Num_List)
    Largest_Num = Num_List[0]
    for i in range(n):
            if(Num_List[i]>Largest_Num):
                Largest_Num = Num_List[i]
    print(Largest_Num)
    return Largest_Num
    
Num_List = [34, 67, 12, 89, 5]
Find_Largest(Num_List)