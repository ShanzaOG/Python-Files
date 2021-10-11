import numpy as np
data = [24,23,43,1,4,45,56,32,54,67,34,31,67,65,45,78]
print("mean:",np.mean(data))
print("median:",np.median(data))
print("50th percentile(median):",np.percentile(data,50))
print("25th percentile:",np.percentile(data,25))
print("75th percentile:",np.percentile(data,75))
print("Standard deviation:",np.std(data))
print("Variance:",np.var(data))