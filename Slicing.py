# Given a list of numbers, extract the first, third, and last elements

# def Extraction(Test_String):
#     Extracted_List  = Test_String[::2]
#     print(Extracted_List)
#     return Extracted_List
    
# Test_String = [10,20,30,40,50]
# Extraction(Test_String)

# def extraction(Test_String):
#     Extracted_List  = [Test_String[0],Test_String[2],Test_String[-1]]
#     print(Extracted_List)
#     return Extracted_List
    
# Test_String = [10,20,30,40,50]
# extraction(Test_String)


#Type2 

# def extraction(Test_String):
#     Extracted_List  = Test_String[::-1]
#     print(Extracted_List)
#     return Extracted_List
    
# Test_String = [1,2,3,4,5]
# extraction(Test_String)

#Type3

# def extraction(Test_String):
#     Extracted_List  = Test_String[1:5]
#     print(Extracted_List)
#     return Extracted_List
    
# Test_String = "programming"
# extraction(Test_String)

#Type4

# def extraction(Test_String):
#     middle = len(Test_String)//2
#     First_Half = Test_String[:middle]
#     Second_Half =  Test_String[middle:]
#     print("First half:",First_Half, "Second half:", Second_Half)
#     return First_Half,Second_Half
    
# Test_String = [1, 2, 3, 4, 5, 6, 7]
# extraction(Test_String)

#Type 5
# def extraction(Test_String):
#     n = len(Test_String)
#     Extract_Num = Test_String[1::2]
#     print(Extract_Num)
#     return Extract_Num
    
# Test_String = [5, 10, 15, 20, 25, 30, 35]
# extraction(Test_String)

#type 6 
# def extraction(Test_String):
#     n = len(Test_String)
#     Extract_Num = Test_String[1::2]
#     print(Extract_Num)
#     return Extract_Num
    
# Test_String = [5, 10, 15, 20, 25, 30, 35]
# extraction(Test_String)


#Type 7
# def extraction(Test_String):
#     n = len(Test_String)
#     Reverse_String = Test_String.split()[::-1]
#     l = []
#     for i in Reverse_String:
#         l.append(i)
#     print(" ".join(l))
#     return 
    
# Test_String = ("Hello World from Python")
# extraction(Test_String)

# Type 8
# def extraction(Test_String):
#     l = Test_String.split(",")
#     print(l, type(l))
#     return Test_String
    
# Test_String = ("I,am,Neharika,Bawdhankar")
# extraction(Test_String)

#type 8

# def extractMid(Text):
#     n = len(Text)
#     Middle = n//2
#     if(n%2==0):
#         NewText = Text[Middle-1:Middle+1]
#     else:
#         NewText = Text[Middle]
#     print(NewText)
#     return NewText
    
# Text = "abcdef"
# extractMid(Text)

# Problem 9: Rotate a List
# Rotate a list by n positions to the left.

# def rotateList(Lis,n):
#     Rt_List = Lis[n:] + Lis[:n]
#     print(Rt_List)
#     return Rt_List

    
# Lis = [1, 2, 3, 4, 5, 6]
# n = 2
# rotateList(Lis,n)

#TYPE 10
# def extract_Range(test):
#     Ex_Range = test[3:8]
#     print(Ex_Range)
#     return Ex_Range
    
# test = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# extract_Range(test)

