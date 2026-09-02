name = "mariem"
age = 20 
rank = 10 

print("my name is:" + name)
# print("my name is: " + name "and my age is : " + age) # type error 

print("my name is: %s" % "mariem")
# print("my name is: %s" % name)
# print("my name is: %s and my age is: %d" %(name, age))
# print("my name is: %s and my age is: %d and my rank is: %f" % (name , age , rank))

# %s => string
# %d => number
# %f => float 

print("my name is: {}" .format("meriem"))
print("my name is: {}" .format(name))
print("my name is: {} and my age is: {}" .format(name, age))
print("my name is: {:s} and my age is: {:d} and my rank is: {:f}" .format (name , age , rank))

# {:s} => string
# {:d} => number
# {:f} => float 

n = "mariem"
l = "python"
y = 12

print("my name's {:s} iam {:s} student with {:d} years EXP" .format (n , l , y))

# control floating point number 

mynumber = 10
print("my number is: {:d}" .format(mynumber))
print("my number is: {:f}" .format(mynumber))
print("my number is: {:.2f}" .format(mynumber)) # . + num controls the number of digits after the decimal point

# truncate string

mylongstring = "hello people of elzero web school i love you all"
print("message is {:s}" .format(mylongstring))
print("message is {:.5s}" .format(mylongstring))
print("message is {:.13s}" .format(mylongstring))

# format money

mymoney = 500162350198

print("my money in bank is: {}" .format(mymoney))
print("my money in bank is: {:_d}" .format(mymoney))
print("my money in bank is: {:,d}" .format(mymoney))
# print("my money in bank is: {:&d}" .format(mymoney)) invalid format 

# rearrange items

a , b , c = "one" , "two" , "three"
print("hello {} {} {}" .format(a , b , c)) # hello one two three 
print("hello {1} {2} {0}" .format(a , b , c)) # hello two three one 
print("hello {2} {0} {1}" .format(a , b , c)) # hello three one two 

x , y , z = "one" , "two" , "three"
print("hello {} {} {}" .format(x , y , z)) # hello one two three 
print("hello {1:d} {2:d} {0:d}" .format(x , y , z)) # hello two three one 
print("hello {2:.2f} {0:.4f} {1:.5f}" .format(x , y , z)) # hello three one two 

# format in version 3.6+

myname = "mariem"
myage = 20

print("my name is : {myname} and my age is : {myage}")
print(f"my name is : {myname} and my age is : {myage}")
