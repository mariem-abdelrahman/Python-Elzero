# O. Calculator
# time limit per test
# 1 second
# memory limit per test
# 256 megabytes

# Given a mathematical expression. The expression will be one of the following expressions: A+B, A−B, A∗B and A/B.

# Print the result of the mathematical expression.
# Input

# Only one line contains A,S and B (1≤A,B≤104), S is either (+,−,∗,/).
# Output

# Print the result of the mathematical expression.
# Examples
# Input

# 7+54

# Output

# 61

# Input

# 17*10

# Output

# 170

# Note

# For the dividing operation you should print the division without any fractions.




s = input()

if "+" in s :
    a , b = s.split("+")
    print(int(a)+int(b))
elif "-" in s :
    a , b = s.split("-")
    print(int(a)-int(b))
elif "*" in s :
    a , b = s.split("*")
    print(int(a)*int(b))
elif "/" in s :
    a , b = s.split("/")
    print(int(a)//int(b))
else :
    print("Invalid input")
    