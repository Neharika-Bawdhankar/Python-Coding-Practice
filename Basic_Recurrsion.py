#Example1
# print name n times using a recursion function
# def printname(nam,n):
#     if(n==0):
#         return
#     print(nam)
#     printname(nam,n-1)
            
# nam = input("Enter name")
# n = int(input("How many times do you want to print the name:"))
# printname(nam,n)

#Example2
#print 1 to n using recursion
# def printonetoN(i,n):
#     if(i>n):
#         return
#     print(i)
#     printonetoN(i+1,n)
       
# n = int(input("How many times do you want to print the name:"))
# printonetoN(1,n)


# #Example3
# #print 1 to n using recursion
# def printN(n):
#     if(n==0):
#         return
#     print(n)
#     printN(n-1)
    
# n = int(input("How many times do you want to print the name:"))
# printN(n)


#Example4
# to print the sum of n numbers

def printSum(i,n):
    if(i>n):
        return
   # sum = sum + i  ////////////why not this????
    ans = printSum(i+1,n)+1
    return ans
ans= printSum(1,4)
print(ans)


