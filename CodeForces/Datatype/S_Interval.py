# S. Interval
# time limit per test
# 1 second
# memory limit per test
# 256 megabytes

# Given a number X. Determine in which of the following intervals the number X belongs to:

# [0,25], (25,50], (50,75], (75,100]

# Note:

#     if X belongs to any of the above intervals print "Interval " followed by the interval.
#     if X does not belong to any of the above intervals print "Out of Intervals".
#     The symbol '(' represents greater than.
#     The symbol ')' represents smaller than.
#     The symbol '[' represents greater than or equal.
#     The symbol ']' represents smaller than or equal. 

# For example:

# [0,25] indicates numbers between 0 and 25.0000, including both.

# (25,50] indicates numbers greater than 25: (25.00001) up to 50.0000000.
# Input

# Only one line containing a number X ( - 1000 ≤ X ≤ 1000).
# Output

# Print the answer to the problem above.
# Examples
# Input

# 25.1

# Output

# Interval (25,50]

# Input

# 25.0

# Output

# Interval [0,25]

# Input

# 100.0

# Output

# Interval (75,100]

# Input

# -25.2

# Output

# Out of Intervals


# [0,25]من اكبر من او يساوي الصفر الي اقل من او يساوي 25 
# (25,50] من اكبر من ال25 الي اقل من او يساوي 50 
# (50,75]من اكبر من 50 الي اقل من او يساوي 75
# (75,100]من اكبر من 75 الي اقل من او يساوي 100 

x = float(input())

if x >= 0 and x <= 25 :
    print("Interval [0,25]")
elif x > 25 and x <= 50 :
    print("Interval (25,50]")
elif x > 50 and x <= 75 :
    print("Interval (50,75]")
elif x > 75 and x <= 100 : 
    print("Interval (75,100]")
else :
    print("Out of Intervals")