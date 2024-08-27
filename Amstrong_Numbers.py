num = int(input("Enter the number:"))
n = num
revnum = 0
numlenght = len(str(num))
while n > 0:
    ldigit = n % 10
    anum = ldigit**numlenght
    print(type(num))
    print("anum=",anum)
    revnum += anum
    print("revnum=",revnum)
    n = n // 10
if(num==revnum):
    print("True : It is a Amstrong number")
else:
    print("False: It is not an Amstrong number")
