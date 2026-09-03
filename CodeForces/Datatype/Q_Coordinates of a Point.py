# Q. Coordinates of a Point
# time limit per test
# 1 second
# memory limit per test
# 256 megabytes

# Given two numbers X, Y which donate coordinates of a point in 2D plan. Determine in which quarter does it belong.

# Note:

#     Print Q1, Q2, Q3, Q4 according to the quarter in which the point belongs to.
#     Print "Origem" If the point is at the origin.
#     Print "Eixo X" If the point is over X axis.
#     Print "Eixo Y" if the point is over Y axis. 

# Input

# Only one line containing two numbers X, Y ( - 1000 ≤ X, Y ≤ 1000).
# Output

# Print the answer to problem above.
# Examples
# Input

# 4.5 -2.2

# Output

# Q4

# Input


# 0.1 0.1

# Output

# Q1




x , y = input().split()

if float(x) == 0 and float(y) == 0 :
    print("Origem")
elif float(x) > 0 and float(y) == 0 :
    print("Eixo X")
elif float(x) < 0 and float(y) == 0 :
    print("Eixo X")
elif float(x) == 0 and float(y) > 0 :
    print("Eixo Y")
elif float(x) == 0 and float(y) < 0 :
    print("Eixo Y")
elif float(x) > 0 and float(y) > 0 :
    print("Q1")
elif float(x) < 0 and float(y) > 0 :
    print("Q2")
elif float(x) < 0 and float(y) < 0 :
    print("Q3")
elif float(x) > 0 and float(y) < 0 :
    print("Q4")
else :
    print("Invalid Input !_!")
