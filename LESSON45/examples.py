# string 

name = "mariem"
print("m" in name)
print("a" in name)
print("A" in name)

# list 

ooo = ["mariem" , "hager" , "roqaya"]
print("mohammed" in ooo)
print("roqaya" in ooo)
print("hager" not in ooo)

# using in and not in with condition 

countriesone = ["egypt" , "ksa" , "kuwait" , "bahrain" , "syria"]
countriesonediscount = 80 

countriestwo = ["italy" , "usa"]
countriestwodiscount = 50 

# mycountry = "egypt"

# if mycountry == "egypt" or mycountry == "ksa" or mycountry == "kuwait" :

#     print(f"hello you have a discount of ${countriesonediscount}")
# else :
#     print("you have no discount")

mycountry = "egypt"
if mycountry in countriesone :

    print(f"hello you have a discount of ${countriesonediscount}")

elif mycountry in countriestwo :

    print(f"hello you have a discount of ${countriestwodiscount}")

else :
    print("you have no discount")