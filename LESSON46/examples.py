# list contains admins 
admins = ["mariem" , "hager" , "mostafa" , "mohammed" , "roqaya" , "abdelrahman" , "mirna"]

# login
name = input("please type your name").strip().capitalize()

# if name is in admin 
if name in admins :

    print(f"hello {name} welcome back")

    option = input("delete or update your name ?").strip().copitalize()

    print(option)

# update option

    if option == "update" or option == "u" :

        thenewname = input("your new name please").strip().capitalize()

        admins[admins.index(name)] = thenewname

        print("name updated.")

        print(admins)

# delete option 

    elif option == "delete" or option == "d" :

        admins.remove(name)

        print("name deleted")   

# wrong option

    else :

        print("wrong option choosed")

else : 

    status = input("not admin, add you  y , n ?").strip().capitalize()

    if status == "yes" or status == "y" :

        print("you have been added")

        admins.append(name)

        print(admins)

    else :

        print("you are not added.")
        