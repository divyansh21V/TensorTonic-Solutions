import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    is_scalar = np.isscalar(x)
    arr = np.asarray(x,dtype=float)
    
    out = 1.0/(1.0+np.exp(-arr))
    return float(out) if is_scalar else out