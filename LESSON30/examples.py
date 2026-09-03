# dictionary

user = {
    "name" : "mariem" ,
    "age" : 20 ,
    "country" : "egypt" ,
    # (1 , 2 , 3 , 4) : "test" ,
    # 1 = "test"
    "skills" : ["html" , "css" , "js"] , 
    "rating" : 10.5
}

print(user)
print(user["country"])
print(user.get("country"))

print(user.keys())
print(user.values())

# two-dimensional dictionary

languages = {
    "one" : {
        "name" : "html" , 
        "progress" : "80%"
    } ,
    "two" : {
            "name" : "css" , 
            "progress" : "90%"
        } ,
        "three" : {
                "name" : "js" , 
                "progress" : "90%"
            } 
}

print(languages)
print(languages["one"])
print(languages["three"])
print(languages["three"]["progress"])
print(languages["three"]["name"])

# dictionary length
print(len(languages))
print(len(languages["two"]))

# create dictionary from variables

frameworkone = {
    "name" : "vuejs" ,
    "progres" : "80%"
}

frameworktwo = {
    "name" : "reactjs" ,
    "progres" : "80%"
}

frameworkthree = {
    "name" : "angular" ,
    "progres" : "80%"
}

allframeworks = {
    "one" : "frameworkone" ,
    "two" : "frameworktwo" ,
    "three" : "frameworkthree"
}

print(allframeworks)