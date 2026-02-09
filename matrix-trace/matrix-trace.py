import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    row=len(A)
    col=len(A[0])
    sum=0
    for i in range(row):
        for j in range(col):
            if(i==j):
                sum+=A[i][j]
    return sum

