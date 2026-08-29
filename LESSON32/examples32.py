# setdefault()

user = {
    "name" : "mariem"
}
print(user)
print(user.setdefault("name" , "mariem"))
print(user)

# popitem()

member = {
    "name" : "mariem" ,
    "skills" : "ps4"
}
print(member)
member.update({"age" : 36})
print(member.popitem())

# items()

view = {
    "name" : "mariem" ,
    "skills" : "xbox"
}

allitems = view.items()
print(view)
view["age"] = 20 

print(allitems)

# fromkeys()

a = ('mykeyone' , 'mykeytwo')
b = "x"

print(dict.fromkeys(a , b))