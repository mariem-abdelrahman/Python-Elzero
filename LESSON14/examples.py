# split() rsplit()

a = "i love python and php and mysql" 
print(a.split()) # split by default space 

b = "i-love-python-and-php-and-mysql"
print(b.split())

b = "i-love-python-and-php-and-mysql"
print(b.split("-"))

c = "i-love-python-and-php-and-mysql"
print(c.split("-",2)) # split by "-" and maxsplit=2

c = "i-love-python-and-php-and-mysql"
print(c.rsplit("-",2))

# center()

e = "mariem"
print(e.center(9)) # spaces 
print(e.center(9,"#")) # hashes

# count()

f = "i love python and php because php is easy"
print(f.count("php"))
print(f.count("php",0,25)) # only one php word

# swapcase()

g = "I Love Python"
h = "i lOVE pYTHON"

print(g.swapcase())
print(h.swapcase())

# startswith()

i = "i love python"
print(i.startswith("i"))
print(i.startswith("s"))
print(i.startswith("p",7,12))

# endswith()

j = "i love python"
print(j.endswith("n"))
print(j.endswith("s"))
print(j.endswith("e",2,6))
