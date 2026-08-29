# tuple with one element 

mytuple1 = ("mariem" ,)
mytuple2 = "mariem" ,

print(mytuple1)
print(mytuple2)

print(type(mytuple1))
print(type(mytuple2))

print(len(mytuple1))
print(len(mytuple2))

# tuple concatenation

a = (1 , 2 , 3 , 4)
b = (5 , 6)

c = a + b 
d = a + ("a" , "b" , True)

print(c)
print(d)

# tuple , list , string repeat (*)

mystring = "mariem"
mylist = [1 , 2]
mytuple = ("a" , "b")

print(mystring * 6)
print(mylist * 6)
print(mytuple * 6)

# methods => count()

a = (1 , 3 , 7 , 8 , 2 , 6 , 5 , 8)
print(a.count(8))

# methods => index()

b = (1 , 3 , 7 , 8 , 2 , 6 , 5)
# print("the position of index is:" + b.index(7)) # error can't concatenate string to num 
print("the position of index is:{:d}" .format(b.index(7)))
print(f"the position of index is:{b.index(7)}")

# tuple destruct

a = ("a" , "b" , "c")

# a = ("a" , "b" , 4 , "c")
# x , y , _ , z = a

# x , y , z = "a" , "b" , "c"
x , y , z = a

print(x)
print(y)
print(z)
