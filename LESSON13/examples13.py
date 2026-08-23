# len()

a = "i love python"
b = "    i love python    "
print(len(a))
print(len(b))

# strip()

a = "    i love python    "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

a = "####i love python####"
print(a.strip("#"))
print(a.rstrip("#"))
print(a.lstrip("#"))

a = "@#@#i love python    "
print(a.strip("@#"))
print(a.rstrip("@#"))
print(a.lstrip("@#"))

# title()

b = "i love 2d graphics and 3g technology and python"
print(b.title())

# capitalize()

b = "i love 2d graphics and 3g technology and python"
print(b.capitalize())

# zfill()

c , d , e , f = "1" , "11" , "111" , "1111"

print(c)
print(d)
print(e)
print(f)

print(c.zfill(3))
print(d.zfill(3))
print(e.zfill(3))
print(f.zfill(3))

# upper()

g = "meriem"
print(g.upper())

# lower()

h = "MERIEM"
print(h.lower())
