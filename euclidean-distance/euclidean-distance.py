import numpy as np

def euclidean_distance(x, y):
    x = np.array(x).reshape(-1)
    y = np.array(y).reshape(-1)
    if(len(x)!=len(y)):
        raise ValueError()
    
    ans = 0.0
    for i in range(len(x)):
        diff = x[i] - y[i]
        ans += diff * diff
    
    return float(ans ** 0.5)
