# append()

myfriends = ["mariem" , "abdelrahman" , "mohammed"]
myoldfriends = ["hager" , "mostafa" , "roqaya"]

myfriends.append("mahmoud")
myfriends.append(100)
myfriends.append(150.200)
myfriends.append(True)
myfriends.append(myoldfriends)

print(myfriends) # whole list
print(myfriends[2]) # abdelrahman
print(myfriends[6]) # True
print(myfriends[7]) # ['hager' , 'mostafa' , 'roqaya']
print(myfriends[7][2]) # roqaya

# extend()

a = [1 , 2 , 3 , 4]
b = ["a" , "b" , "c"]
c = ["one" , "two"]

a.extend(b)
a.extend(c)

print(a)

# remove 

x = [1 , 2 , 3 , 4 , 5 , "mariem" , True , "mariem" , "mariem"]
x.remove("mariem")
print(x)

# sort()

y = [1 , 2 , 100 , 120 , -10 , 17 , 29]
# y = [1 , 2 , 100 , 120 , -10 , 17 , 29 , "mariem"] error just one type of values
# y = ["a" , "z" , "c"]

y.sort() # (reverse=False)
print(y)
y.sort(reverse=True)
print(y)

#reverse()

z = [10 , 1 , 9 , 80 , 100 , "mariem" , 100]
z.reverse()
print(z)
