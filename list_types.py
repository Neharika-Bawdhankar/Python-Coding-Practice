names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)



l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
# l.append(7)
# l.sort(reverse=True)
# l.reverse()
# print(l.index(1))
# print(l.count(1))
m = l
m[0] = 0
# l.insert(1, 899)
# m = [900, 1000, 1100]
# k = l + m
# # print(k)
# # l.extend(m)
print(m)