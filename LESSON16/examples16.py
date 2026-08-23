# replace(old value , new value , count)

a = "hello one two three one one"
print(a.replace("one" , "1"))
print(a.replace("one" , "1" , 1))
print(a.replace("one" , "1" , 2))

# join(iterable)

mylist = ["mariem" , "abdelrahman" , "mohammed"]
print("-".join(mylist))
print(" ".join(mylist))
print(",".join(mylist))
print(type(",".join(mylist)))