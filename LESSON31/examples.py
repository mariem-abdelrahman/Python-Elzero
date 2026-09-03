# clear()
user = {
    "name" : "mariem"
}
print(user)
user.clear()
print(user)

# update()

member ={
    "name" : "mariem"
}
print(member)
member["age"] = 20
print(member)
member.update({"country" : "egypt"})
print(member)

# copy()

main = {
    "name" : "mariem"
}

b = main.copy()
print(b)
main.update({"skills" : "fighting"})
print(main) # shallow copy
print(b)

# keys() + values()

print(main.keys())
print(main.values())