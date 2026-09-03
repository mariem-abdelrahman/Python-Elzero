# R. Age in Days
# time limit per test
# 1 second
# memory limit per test
# 256 megabytes

# Given a Number N corresponding to a person's age (in days). Print his age in years, months and days, followed by its respective message "years", "months", "days".

# Note: consider the whole year has 365 days and 30 days per month.
# Input

# Only one line containing a number N (0 ≤ N ≤ 106).
# Output

# Print the output, like the following examples.
# Examples
# Input

# 400

# Output

# 1 years
# 1 months
# 5 days

# Input

# 800

# Output

# 2 years
# 2 months
# 10 days

# Input

# 30

# Output

# 0 years
# 1 months
# 0 days



n = int(input())

ay = n / 365 
print(f"{int(ay)} years")

j = (int(n)-(int(ay)*365))/30
print(f"{int(j)} months")

t = int(n)-((int(ay)*365)+(int(j)*30))
print(f"{int(t)} days")
