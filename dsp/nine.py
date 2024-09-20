import numpy as np
def corr(x, y):
    correlation_matrix = np.corrcoef(x, y)
    return correlation_matrix

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
print(corr(x,y))
