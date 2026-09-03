# note 
print("#" * 80)
print(" you can write the first letter or full name of the time unit ".center(80,"-"))
print("#" * 80)

# collect age data 

age = int(input("please write your age").strip())

# collect time unit data 
unit = input("please choose time unit : months , weeks , days").strip().lower()

# get time units
months = age * 12
weeks = months * 4 
days = age * 365 

if unit == "months" or unit == "m" :

    print("you choosed the unit months")
    print(f"you lived for {months:,} months.")

elif unit == "weeks" or unit == "w" : 
    
    print("you choosed the unit weeks")
    print(f"you lived for {weeks:,} weeks.")

elif unit == "days" or unit == "d" : 
    
    print("you choosed the unit days")
    print(f"you lived for {days:,} days.")
