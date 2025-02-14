#code works on both cluster and single node but not parallelizable so ray doesn't use 2nd cluster node for tasks
from numba import jit, cuda
import ray
import numpy as np
# to measure exec time
from timeit import default_timer as timer

# normal function to run on cpu
def func(a):
    for i in range(10000000):
        a[i]+= 1

# function to run on cluster with ray
@ray.remote
def func3(a):
    # it seems you just can't pass array a becuase it is on the global shared memory store, I cheated and just rebuild t
he array as part of the function
    a = np.ones(10000000, dtype = np.float64)
    for i in range(10000000):
        a[i]+= 1


# function optimized to run on gpu
@jit
def func2(a):
    for i in range(10000000):
        a[i]+= 1

if __name__=="__main__":
    n = 10000000
    a = np.ones(n, dtype = np.float64)

    for i in range(3):
        start = timer()
        func(a)
        print("without GPU:", timer()-start)

    for i in range(50):
        start = timer()
        func2(a)
        print("with GPU:", timer()-start)

    ray.init()

    for i in range(50):
        start = timer()
        func3.remote(a)
        print("with GPU on 2 node ray cluster:", timer()-start)
