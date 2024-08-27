#patterns

def nForest(n:int) ->None:
    # Write your solution here.
    #n = 5  # Number of rows and columns
    for i in range(n):  # Outer loop for rows
        for j in range(n):  # Inner loop for columns
            print("*", end=" ")
        print()  # Move to the next line after each row  
    # pass



#pattern2
def nForest(n:int) ->None:
    # Write your solution here.
    for i in range(n):
        for j in range(i+1):
            print("* ",end="")
        print()
    #pass


#patterns3

def nTriangle(n:int) ->None:
    # Write your solution here.
    for i in range(n):
        for j in range(i+1):
            print(j+1," ",end="")
        print()
    #pass

#pattern4
def seeding(n: int) -> None:
    for i in range(n):
        for j in range(n-i):
            print("* ",end="")
        print()
    #pass

#pattern 5

def triangle( n:int) ->None:
    # Write your solution here.
    for i in range(n):
        for j in range(i+1):
            print(i+1," ",end="")
        print()
    #pass

#pattern 6

def nStarTriangle(n: int) -> None:
    # Write your code here.
    for i in range(n):
        for j in range(n-1-i):
            print(" ", end="")
        for j in range(2*i+1):
            print("*",end="")
        print()
    pass

