x = 52
print(f"This is global variable in function gobalvar x = {x}") 


def gobalvar():
    global x
    x = 984564564
    y = 789
    
    print(f"This is local variable in function gobalvar x = {x}")
    print(f"This is local variable in function gobalvar x = {y}")
    
gobalvar()
# now the value of x is changed in function
print(f"This is global variable in function gobalvar x = {x}")