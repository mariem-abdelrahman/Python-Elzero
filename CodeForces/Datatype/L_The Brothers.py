# L. The Brothers
# time limit per test
# 1 second
# memory limit per test
# 256 megabytes

# Given two person names.

# Each person has {"the first name" + "the second name"}

# Determine whether they are brothers or not.

# Note: The two persons are brothers if they share the same second name.
# Input

# First line will contain two Strings F1, S1 which donates the first and second name of the 1st person.

# Second line will contain two Strings F2, S2 which donates the first and second name of the 2nd person.
# Output

# Print "ARE Brothers" if they are brothers otherwise print "NOT".
# Examples
# Input

# bassam ramadan
# ahmed ramadan

# Output

# ARE Brothers

# Input

# ali salah
# ayman salah

# Output

# ARE Brothers

# Input

# ali kamel
# ali salah

# Output

# NOT


f1 , s1 = input().split()
f2 , s2 = input().split()

if s1 == s2 :
    print("ARE Brothers")
else :
    print("NOT")