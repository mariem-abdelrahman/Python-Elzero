# str()

a = 10 
print(type(a))
print(type(str(a)))

# tuple()

c = "mariem" # string
d = [1 , 2 , 3 , 4 , 5] # list
e = {"a" , "b" , "c"} # set
f = {"a" : 1 , "b" : 2} # dictionary

print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))
# print(tuple(500)) # error iterable

# list()

c = "mariem" # string
d = (1 , 2 , 3 , 4 , 5) # tuple
e = {"a" , "b" , "c"} # set
f = {"a" : 1 , "b" : 2} # dictionary

print(list(c))
print(list(d))
print(list(e))
print(list(f))

# set()

c = "mariem" # string
d = (1 , 2 , 3 , 4 , 5) # tuple
e = ["a" , "b" , "c"] # list
f = {"a" : 1 , "b" : 2} # dictionary

print(set(c))
print(set(d))
print(set(e))
print(set(f))

# dict()

# c = "mariem" # string # error there is no key & value 
# d1 = (1 , 2 , 3 , 4 , 5) # tuple # error 
d = (("a" , 1) , ("b" , 2) , ("c" , 3)) # nested tuple is ok 
# e1 = ["a" , "b" , "c"] # list # error 
e = [["one" , 1] , ["two" , 2] , ["three" , 3]] # list
# f = {"a" : 1 , "b" : 2} # set # error # un hashable type

# print(dict(c))
print(dict(d))
print(dict(e))
# print(dict(f))