# C. Simple Calculator
# time limit per test
# 1 second
# memory limit per test
# 256 megabytes

# Given two numbers X and Y. Print the summation and multiplication and subtraction of these 2 numbers.
# Input

# Only one line containing two separated numbers X, Y (1  ≤  X, Y  ≤  105).
# Output

# Print 3 lines that contain the following in the same order:

#     "X + Y = summation result" without quotes.
#     "X * Y = multiplication result" without quotes.
#     "X - Y = subtraction result" without quotes. 

# Example
# Input

# 5 10

# Output

# 5 + 10 = 15
# 5 * 10 = 50
# 5 - 10 = -5

# Note

# Be careful with spaces.







num1 , num2= input().split()

print(f"{num1} + {num2} = {int(num1)+int(num2)}")
print(f"{num1} * {num2} = {int(num1)*int(num2)}")
print(f"{num1} - {num2} = {int(num1)-int(num2)}")