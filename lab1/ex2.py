import numpy as np
import time

k=3
x = np.random.random(size=k)
y = np.random.random(size=k)
print(f"Vector x: {x}")
print(f"Vector y: {y}\n")

#calculating the scalar product
print(f"Result of calculating the scalar product x and y: {np.vdot(x, y)}\n")

# numpy
t1 = time.time()
print(f"Max element of vector x by method with numpy: {np.max(x)}")
print(f"Min element of vector x by method with numpy: {np.min(x)}\n")
t2 = time.time()
x = x.tolist()
print(f"Max element of vector x by method with python syntax: {max(x)}")
print(f"Min element of vector x by method with python syntax: {min(x)}\n")
t3 = time.time()
dt = t2 - t1
dt2 = t3 - t2

print(f"Time taken for numpy operations: {dt:.6f} seconds")
print(f"Time taken for Python operations: {dt2:.6f} seconds\n")

print(f"Mathematical expectation for vector x: {np.mean(x)}")
print(f"Mathematical expectation for vector y: {np.mean(y)}\n")

print(f"Variance for vector x: {np.var(x)}")
print(f"Variance for vector y: {np.var(y)}")

