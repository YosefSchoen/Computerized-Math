import numpy as np

# Assign the matrix A and vector b values in Eq.(1.2) above
A = np.array([[5, 4, 3, -1], [-4, -1, 7, 7], [3, 1, 9, -2], [2, 8, -4, -3]], dtype='float')
b = np.array([7, 1, 4, 6])

# Form the augmented matrix (A|b)
Ab = np.hstack([A, b.reshape(-1, 1)])

print("\nAb=" , Ab, "\n")

# Assign the number of eqns to the variable n
n = len(b)

for i in range(n):
    # assign to `a' the next row in

    #   Ab = ( 	a11,	a12,	a13 |	b1
    # 			a21,	a22,	a23 |	b2
    # 			a31,	a32,	a33 |	b3 )

    # e.g. if i=0,
    # 	a = (	a11,	a12,	a13 |	b1 ).

    a = Ab[i]

    for j in range(i + 1, n):
        # assign to `b' the next row after `a', e.g. if i=0 and j=1,
        # b = Ab[j=1] = (	a21,	a22,	a23 |	b2 ).

        b = Ab[j]
        m = a[i] / b[i]		# m		= a11 / a21

        # Now re-declare Ab[j=1]
        # Ab[j=1] = a -m*b
        #         = ( a11, a12, a13 | b1 ) - (a11 / a21)* ( a21, a22, a23 | b2 )
        #         = ( 0,a12-m*a22, a13-m*a23 | b1-m*b2)

        Ab[j] = a - m * b

        for i1 in range(n):
            for j1 in range(n+1):
                print("%.1f" % Ab[i1][j1], "\t", end='')
            print("\n")
        print("\n")
        # Continuing in this way brings the augmented matrix Ab into echelon form.

# Print Ab to show it in echelon form:

print("\nAb = ")

for i in range(n):
    for j in range(n+1):
        print("%.1f" % Ab[i][j], "\t", end='')
    print("\n")

print(" in row echelon form.\n")

# Starting from the last row in Ab, reduce it from echelon form to the form

# (1,0,0|b1
#  0,1,0|b2
#  0,0,1|b3)

for i in range(n - 1, -1, -1):
    Ab[i] = Ab[i] / Ab[i, i]
    a = Ab[i]

    for j in range(i - 1, -1, -1):
        b = Ab[j]
        m = a[i] / b[i]
        Ab[j] = a - m * b

        for i1 in range(n):
            for j1 in range(n+1):
                print("%.1f" % Ab[i1][j1],"\t", end='')
            print("\n")
        print("\n")
# Print Ab to show it the form

# (1,0,0|b1
#  0,1,0|b2
#  0,0,1|b3)

print("\nAb = ")
for i in range(n):
    for j in range(n+1):
        print("%.1f" % Ab[i][j],"\t", end='')
    print("\n")

# From the final form of Ab, print the solution to the equation.

print("The answer is v= \n")

# Assign to x the solution to the equation

x = Ab[:, 3]

print(x)
