# difference()

a = {1 , 2 , 3 , 4}
b = {1 , 2 , "mariem" , "abdelrahman"}
print(a)
print(a.difference(b)) # a - b 
print(a)

print("-+-" * 40)

# difference_update()

c = {1 , 2 , 3 , 4}
d = {1 , 2 , "mariem" , "abdelrahman"}
print(c)
print(c.difference_update(d)) # c - d 
print(c)

print("-+-" * 40)

# intersection()

e = {1 , 2 , 3 , 4 , "x"}
f = {"mariem" , "x" , 2}
print(e)
print(e.intersection(f)) # e & f
print(e)

print("-+-" * 40)

# intersection_update()

g = {1 , 2 , 3 , 4 , "x"}
h = {"mariem" , "x" , 2}
print(g)
print(g.intersection_update(g)) # g & h
print(g)

print("-+-" * 40)

# symmetric_difference()

i = {1 , 2 , 3 , 4 , 5 , "x"}
j = {"mariem" , "zero" , 1 , 2 , 4}
print(i)
print(i.symmetric_difference(j)) # i ^ j
print(i)

print("-+-" * 40)

# symmetric_difference_update()

k = {1 , 2 , 3 , 4 , 5 , "x"}
l = {"mariem" , "zero" , 1 , 2 , 4}
print(k)
print(k.symmetric_difference(j)) # k ^ l
print(k)

