# indexing ( access single item )
mystring = "i love python"

print(mystring[0])  # index 0 => i
print(mystring[9]) # index 9 => t

print(mystring[-1]) # index -1 => first character from the end => n
print(mystring[-6]) # index -6 => 6th character from the end => v

# slicing ( access multiple sequential items )

print(mystring[8:11])  # yth
print(mystring[3:5])   # ov

print(mystring[:10]) # if start is not here will start from 0 => i love pyt
print(mystring[5:]) # if end is not here will go to the end => e python

print(mystring[:]) # full data 

print(mystring[0::1]) # full data
print(mystring[::1]) # full data

print(mystring[::2]) # i oepyo 
print(mystring[::3]) # i lph