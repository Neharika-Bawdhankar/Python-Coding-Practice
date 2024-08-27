# s = {1,4,4,3,2,1, 2, 6}
# print(s)

# info = {"Carla", 19, False, 5.9, 19}
# # print(info)

# harry = set()
# # print(type(harry)) 

# for value in info:
#   # print(value)
  
# S1 = {1,3,5,7,9}
# S2 = {1,3,8}
# # print(S1.union(S2))  
# # print(S1.intersection(S2))
# # S1.intersection_update(S2)
# print(S1.symmetric_difference(S2))
# # S1.update(S2)
# print(S1,S2)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Seoul")
print(cities)

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")