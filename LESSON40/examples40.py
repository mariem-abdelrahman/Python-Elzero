# input age 

age = int(input("what's your age ?").strip())

# get age in all time units

months = age * 12
weeks = months * 4 
days = age * 365 
hour = days * 24 
minutes = hour * 60 
seconds = minutes * 60 

print("your lived for : ")
print(f"{months} months.")
print(f"{weeks} weeks.")
print(f"{days:_} days.")
print(f"{minutes:_} minutes.")
print(f"{seconds:_} seconds.")
