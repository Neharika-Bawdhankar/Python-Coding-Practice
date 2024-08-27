def count(n):
    #print("value is",n)
    count = 0
    while n > 0:
        count = count + 1
        #print(count)
        n=n//10
    return count

n = int(input("Enter the digit:"))
digits = count(n)
print("The total number of digits in entered number is:",digits)


#second method
n = input("Enter the digit:")
digits = len(n)
print("The total number of digits in entered number is:", digits)


