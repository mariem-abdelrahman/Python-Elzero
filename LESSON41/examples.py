uname = "mariem"
ucountry = "egypt"
cname = "python course"
cprice = 100 
cdiscount = 30 

if ucountry == "egypt" : 

    print(f"hello {uname} because you are from {ucountry}")
    print(f"the course \"{cname}\" price is : ${cprice - 80}")

elif ucountry == "ksa" :

    print(f"hello {uname} because you are from {ucountry}")
    print(f"the course \"{cname}\" price is : ${cprice - 10}")

elif ucountry == "kuwait" :

    print(f"hello {uname} because you are from {ucountry}")
    print(f"the course \"{cname}\" price is : ${cprice - 20}")
    
else :

    print(f"hello {uname} because you are from {ucountry}")
    print(f"the course \"{cname}\" price is : ${cprice - 30}")

