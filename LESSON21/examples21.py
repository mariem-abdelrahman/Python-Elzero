myawesomelist = ["one" , "two" , "one" , 1 , 100.5 , True]

print(myawesomelist) # whole list
print(type(myawesomelist[1])) # "one"
print(myawesomelist[-1]) # True
print(myawesomelist[-3]) # 1

print(myawesomelist[1:4]) # ['two' , 'one' , 1]
print(myawesomelist[:4]) # ['one' , 'two' , 'one' , 1]
print(myawesomelist[1:]) # ['two' , 'one' , 1 , 100.5 , True]

print(myawesomelist[::1]) # ['one' , 'two' , 'one' , 1 , 100.5 , True]
print(myawesomelist[::2]) # ['one' , 'one' , 100.5]

# print(myawesomelist[150]) # out of range

print(myawesomelist)
myawesomelist[1] = 2 
myawesomelist[-1] = False
# myawesomelist[0:2] = []
# myawesomelist[0:3] = []
myawesomelist[0:3] = ["A" , "B" , "C"]
myawesomelist[0:3] = ["A" , "B"]
myawesomelist[0:3] = ["A" , "B" , 1 , 2 , 3]
print(myawesomelist)
