
import numpy as np
import time

# Non-optimized version
data_list = list(range(10_000_000))
start = time.time()
total_list = sum(data_list)
end = time.time()
print("List sum time:", end - start)

# Optimized version
data_array = np.arange(10_000_000)
start = time.time()
total_array = np.sum(data_array)
end = time.time()
print("NumPy sum time:", end - start)
