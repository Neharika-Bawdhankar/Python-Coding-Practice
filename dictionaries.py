# dict = {"Name":"Neharika","Age":"32","Gender":"Female"}
# print(dict['Name'])
# for keys, value in dict:
#     print(f"the value coreesponding to the key {keys} is {value}")
# print(dict)
# print(dict.keys())
# print(dict.values())

# for items in dict:
#     print(items)
# print(dict.items())
# for key, value in dict.items():
#   print(f"The value corresponding to the key {key} is {value}")    
  
  
  
# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info['name'])
# print(info.get('eligible'))

info = {'name':'Karan', 'age':19, 'eligible':True}
info.update({'age':20})
info.update({'name':'Neharika'})
print(info)