# clear()

a = {1 , 2 , 3}
a.clear()
print(a)

# union()

b = {"one" , "two" , "three"}
c = {"1" , "2" , "3"}
x = {"zero" , "cool"}

print(b | c) # without any method 
print(b.union(c))
print(b.union(c , x))

# add()
d = {1 , 2 , 3 , 4}
# d.add(5 , 6) # takes exactly one argument
d.add(5)
d.add(6)
print(d)
# d.add({"mariem" , "hager" , 1 , True}) # error 

# copy()

e = {1 , 2 , 3 , 4}
f = e.copy() # shallow copy

print(e)
print(f)

e.add(6)

print(e)
print(f)

# remove()

g = {1 , 2 , 3 , 4}
g.remove(1)
# g.remove(7) # error 7 not found 
print(g)

# discard()

h = {1 , 2 , 3 , 4}
h.discard(1)
h.discard(7) 
print(h)

# pop()

i = {"a" , True , 1 , 2 , 3 , 4 , 5}
print(i.pop())

# update()

j = {1 , 2 , 3}
k = {1 , "a" , "b" , 2}
j.update(["html" , "css"])
j.update(k)

print(j)
