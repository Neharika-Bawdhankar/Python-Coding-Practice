# Type 11
# Problem 1: Extract the Last 3 Elements
# def extract_Nums(nums):
#     nums1 = nums[-3:]
#     print(nums1)
#     return nums1
    
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# extract_Nums(nums)

# Type 2
# Problem 2: Reverse a String
# def extract_Nums(text):
#     nums1 = text[::-1]
#     print(nums1)
#     return nums1
    
# text = "PythonProgramming"
# extract_Nums(text)

# Type 3
# Problem 3: Extract the First Half
def first_Half(nums):
    n = len(nums)
    mid = n//2
    if(n//2==0):
        test = nums[:mid]
    else:
        mid2 = mid + 1
        test = nums[:mid2]
    print(test)
    return test
         
nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]
first_Half(nums)