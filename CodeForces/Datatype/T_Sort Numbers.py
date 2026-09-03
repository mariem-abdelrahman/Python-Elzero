# T. Sort Numbers
# time limit per test
# 0.25 seconds
# memory limit per test
# 256 megabytes

# Given three numbers A, B, C. Print these numbers in ascending order followed by a blank line and then the values in the sequence as they were read.
# Input

# Only one line containing three numbers A, B, C ( - 106  ≤  A, B, C  ≤  106)
# Output

# Print the values in ascending order followed by a blank line and then the values in the sequence as they were read.
# Examples
# Input

# 3 -2 1

# Output

# -2 \\ الاصغر 
# 1 \\ الاوسط 
# 3 \\ الاكبر 

# 3 \\ الاكبر
# -2 \\ الاصغر 
# 1 \\ الاوسط

# Input

# -2 10 0

# Output

# -2 \\ الاصغر 
# 0 \\ الاوسط 
# 10 \\ الاكبر 

# -2 \\ الاصغر 
# 10 \\ الاكبر 
# 0 \\ الاوسط 


a , b , c = input().split()

print(min(int(a) , int(b) , int(c)))

if int(a) >= int(b) and int(a) <= int(c) :
    print(a)

elif int(a) <= int(b) and int(a) >= int(c) :
    print(a)

elif int(b) >= int(a) and int(b) <= int(c) :
    print(b)
    
elif int(b) <= int(a) and int(b) >= int(c) :
    print(b)
else :
    print(c)


print(max(int(a) , int(b) , int(c)))

print ()

print(a)
print(b)
print(c)
