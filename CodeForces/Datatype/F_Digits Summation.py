# F. Digits Summation
# time limit per test
# 0.25 seconds
# memory limit per test
# 64 megabytes

# Given two numbers N and M. Print the summation of their last digits.
# Input

# Only one line containing two numbers N, M (0 ≤ N, M ≤ 1018).
# Output

# Print the answer of the problem.
# Example
# Input

# 13 12

# Output

# 5

# Note

# First Example :

# last digit in the first number is 3 and last digit in the second number is 2.

# So the answer is: (3 + 2 = 5)





n , m = input().split()

print(int(n)%10 + int(m)%10)