# K. Max and Min
# time limit per test
# 0.25 seconds
# memory limit per test
# 64 megabytes

# Given 3 numbers A, B and C, Print the minimum and the maximum numbers.
# Input

# Only one line containing 3 numbers A, B and C ( - 105 ≤ A, B, C ≤ 105)
# Output

# Print the minimum number followed by a single space then print the maximum number.
# Examples
# Input

# 1 2 3

# Output

# 1 3

# Input

# -1 -2 -3

# Output

# -3 -1

# Input

# 10 20 -5

# Output

# -5 20


a , b , c = input().split()
 
# print(min(int(a) , int(b) , int(c)) , max(int(a) , int(b) , int(c)))

if int(a) <= int(b) and int(a) <= int(c) :
    minn = a 
elif int(b) <= int(a) and int(b) <= int(c) :
    minn = b
else :
    minn = c

if int(a) >= int(b) and int(a) >= int(c) :
    maax = a 
elif int(b) >= int(a) and int(b) >= int(c) :
    maax = b
else :
    maax = c

print(minn , maax)












