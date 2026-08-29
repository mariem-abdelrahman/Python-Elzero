# tuple syntax and type test

myawesometupleone = ("mariem" , "abdelrahman")
myawesometupletwo = "mariem" , "abdelrahman"

print(myawesometupleone)
print(myawesometupletwo)

print(type(myawesometupleone))
print(type(myawesometupletwo))

# tuple indexing

myawesometuplethree = (1 , 2 , 3 , 4 , 5)
print(myawesometuplethree[0])
print(myawesometuplethree[-3])

# tuple assign values

myawesometuplefour = (1 , 2 , 3 , 4 , 5)
myawesometuplefour[2] = "three"
# print(myawesometuplefour) # 'tuple' object deos not support item assignment

# tuple items 

myawesometuplefive = ("mariem" , "abdelrahman" , 1 , 2 , 3 , 100.5 , True)
print(myawesometuplefive[1])
print(myawesometuplefive[-1])


