# Problem 1: Sum of Numbers
# Write a Python program that takes a list of numbers and returns the sum of all the numbers.


def Sum_All():
    n = len(list1)
    AddSum = 0
    for i in range (n):
        # print("list value is :", list1[i])
        AddSum += list1[i]
        # print("Sum is :", sum)
    print(AddSum)
    return AddSum

list1 = [4,5,9,7,3,11,55]
Sum_All()