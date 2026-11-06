import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A = np.asarray(A)
    rows , cols  = A.shape
    output = np.zeros((cols,rows),dtype=A.dtype)
    for i in range(rows):
        for j in range(cols):
            output[j][i] = A[i][j]

    return output