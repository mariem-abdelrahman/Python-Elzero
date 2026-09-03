# clear()

a = [1 , 2 , 3 , 4]
a.clear()
print(a)

# copy()

b = [1 , 2 , 3 , 4]
c = b.copy()
print(b) # main list
print(c) # copied list

b.append(5)

print(b) # main list
print(c) # copied list # shallow copy # just from the origenal list # there is no editing no abdate






# ========================================================================================










# # deepcopy()

# import copy
# b = [1 , 2 , 3 , 4]
# c = copy.deepcopy(b)
# print(b) # main list
# print(c) # copied list

# b.append(5)

# print(b) # main list
# print(c) # copied list # deep copy # editing & abdates is available







# ============================================================================================














# count()

d = [1 , 2 , 3 , 4 , 3 , 9 , 10 , 1 , 2 , 1]
print(d.count(1))

# index()

e = ["meriem" , "abdelrahman" , "mohammed" , "hager" , "roqaya" , "hager"]
print(e.index("hager"))

# insert()

f = [1 , 2 , 3 , 4 , 5 , "a" , "b"]
f.insert(0 , "test")
print(f)
f.insert(-1 , "test")
print(f)

# pop() 

g = [1 , 2 , 3 , 4 , 5 , "a" , "b"]
print(g.pop(-1))

# print(g[0:3]) # slicing # range
