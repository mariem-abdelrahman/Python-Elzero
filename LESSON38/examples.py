fname = input("what is your first name")
mname = input("what is your middle name")
lname = input("what is your last name")

fname = fname.strip().capitalize()
mname = mname.strip().capitalize()
lname = lname.strip().capitalize()

print(f"hello {fname} {mname:1s} {lname} happy to see you.")