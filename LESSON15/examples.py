# index(substring,start,end)

a = "i love python"
print(a.index("p")) # index number 7
print(a.index("p",0,10)) # index number 7
# print(a.index("p",0,5)) # error because p is not in the range 0 to 7

# find(substring,start,end)

b = "i love python"
print(b.find("p")) # index number 7
print(b.find("p",0,10)) # index number 7
print(b.find("p",0,5)) # -1 because p is not in the range 0 to 7

# rjust(width, fill char) ljust(width, fill char)

c = "mariem"
print(c.rjust(12)) # spaces
print(c.rjust(12,"#")) # hashes

d = "mariem"
print(d.ljust(12)) # spaces
print(d.ljust(12,"#")) # hashes

splitlines() 

e = """first line
second line
third line"""

print(e.splitlines())

f = "first line\nsecond line\nthird line"
print(f.splitlines())

# expandtabs()

g = "hello\tworld\ti\tlove\tpython"
print(g.expandtabs(8))

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())
print(two.istitle())

three = " "
four = ""
print(three.isspace())
print(four.isspace())

five = 'i love python'
six = 'I Love Python'
print(five.islower())
print(six.islower())

seven = "mariem_abdo"
eight = "Mariem_Abdo90"
nine = "Mariem--Abdo90"

print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"
print(x.isalpha())
print(y.isalpha())

u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"
print(u.isalnam())
print(z.isalnam())
