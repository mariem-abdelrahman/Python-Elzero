# H. Two numbers
# time limit per test
# 1 second
# memory limit per test
# 256 megabytes

# Given 2 numbers A and B. Print floor, ceil and round of A/B

# Note:

#     Floor: Is a mathematical function that takes a real number X and its output is the greatest integer less than or equal to X.
#     Ceil: Is a mathematical function that takes a real number X and its output is the smallest integer larger than or equal to X.
#     Round: Is a mathematical function that takes a real number X and its output is the closest integer to that number X. 

# For more clarification visit the links in the notes below.
# Input

# Only one line containing two numbers A and B (1≤A,B≤103)
# Output

# Print 3 lines that contain the following in the same order:

#     "floor A / B = Floor result" without quotes.
#     "ceil A / B = Ceil result" without quotes.
#     "round A / B = Round result" without quotes. 

# Examples
# Input
# Copy

# 10 3

# Output
# Copy

# floor 10 / 3 = 3
# ceil 10 / 3 = 4
# round 10 / 3 = 3

# Input
# Copy

# 10 4

# Output
# Copy

# floor 10 / 4 = 2
# ceil 10 / 4 = 3
# round 10 / 4 = 3

# Input
# Copy

# 10 6

# Output
# Copy

# floor 10 / 6 = 1
# ceil 10 / 6 = 2
# round 10 / 6 = 2

# Note

# Links:

#     For Rounding method visit: https://www.mathsisfun.com/numbers/rounding-methods.html.
#     For Flooring and Ceiling method visit: https://www.mathsisfun.com/sets/function-floor-ceiling.html. 

import math

a , b = input().split()

print(f"floor {a} / {b} = {math.floor(int(a)/int(b))}")
print(f"ceil {a} / {b} = {math.ceil(int(a)/int(b))}")

r = (int(a) / int(b)) - (int(a) // int(b))
if r >= 0.5 :
    print(f"round {a} / {b} = {(int(a)//int(b)) + 1}")
else :
    print(f"round {a} / {b} = {(int(a)//int(b))}")


