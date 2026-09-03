# issuperset()

a = {1 , 2 , 3 , 4}
b = {1 , 2 , 3}
c = {1 , 2 , 3 , 4 , 5}

print(a.issuperset(b)) # true 
print(a.issuperset(c)) # false

print("=" * 40)

# issubset()

d = {1 , 2 , 3 , 4}
e = {1 , 2 , 3}
f = {1 , 2 , 3 , 4 , 5}

print(a.issubset(e)) # false
print(a.issubset(f)) # true

print("=" * 40)

# isdisjoint()

g = {1 , 2 , 3 , 4}
h = {1 , 2 , 3}
i = {10 , 11 , 12}

print(g.isdisjoint(h)) # false
print(g.isdisjoint(i)) # true
