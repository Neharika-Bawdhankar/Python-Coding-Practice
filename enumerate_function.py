# fruits = ['apple','mangoes','berries','litchi']
# index = 0
# for name in fruits:
#     if index == 2:
#         print("You got an ", name)
#     else:
#          print(name)
#     index +=1


fruits = ['apple','mangoes','berries','litchi']

for index , name in enumerate(fruits):
    if index == 2:
        print("Hurray!!!!!!!! You got an ", name)
    else:
         print(name)
    index +=1