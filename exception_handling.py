# def info():
#     try:
#         list = [1,2,3,4,5]
#         i = int(input("Enter the index value :"))
#         print(list[i])
#         return 1
#     except Exception as e:
#         print(e)
#         return 0
#     finally:
#         print("I am always exceuted")
        
# x = info()     #function is returning a value so x is used 
# print(x)


salary = int(input("Enter the salary:"))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")