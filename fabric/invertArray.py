import numpy as np
N = 4000
import ray
ray.init()

@ray.remote
def f(x):
    arr = np.random.randn(N, N)
    inv_arr = np.linalg.inv(arr)
    return x

futures = [f.remote(i) for i in range(96)]
#print("count =\n", x)
print(ray.get(futures))
