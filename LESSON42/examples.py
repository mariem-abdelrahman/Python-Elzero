uname = "mariem"
isstudent = "yes"
ucountry = "egypt"
cname = "python course"
cprice = 100 
cdiscount = 30 

if ucountry == "egypt" or ucountry == "ksa" or ucountry == "qatar": 

    print(f"hello {uname} because you are from {ucountry}")

    if isstudent == "yes" :

        print(f"hello {uname} because you are from {ucountry}and student")
        print(f"the course \"{cname}\" price is : ${cprice - 90}")

    else :
        
        print(f"hello {uname} because you are from {ucountry}")
        print(f"the course \"{cname}\" price is : ${cprice - 80}")

elif ucountry == "kuwait" or ucountry == "bahrain" :

    print(f"hello {uname} because you are from {ucountry}")
    print(f"the course \"{cname}\" price is : ${cprice - 20}")
    
else :

    print(f"hello {uname} because you are from {ucountry}")
    print(f"the course \"{cname}\" price is : ${cprice - 30}")
