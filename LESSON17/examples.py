# string formatting

name = "mariem"
age = 20
rank = 10 
print("My Name is:" + name)
# print("My Name is:" + name + " and My Age is: " + age) # type error 

print("My Name is: %s" % "Mariem")
print("My Name is: %s" % name)
print("My Name is: %s and My Age is: %d" % (name , age))
print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name , age , rank))

n = "mariem"
l = "python"
y = 12

print("my name's %s iam %s student with %d years EXP" % (n , l , y))

# control floating point number 

mynumber = 10
print("my number is: %d" %mynumber)
print("my number is: %f" %mynumber)
print("my number is: %.2f" %mynumber) # . + num controls the number of digits after the decimal point

# truncate string

mylongstring = "hello people of elzero web school i love you all"
print("message is %s" % mylongstring)
print("message is %.5s" % mylongstring)