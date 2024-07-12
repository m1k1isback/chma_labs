import numpy as np
import time

def function_of_filling(i, j):
    a = 1.0/np.sqrt(pow(i+1, 2)+pow(j+1, 2))
    return a

N = 1000

# Using two nested lists
t1 = time.time()
matrix_A = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        matrix_A[i, j] = 1.0/np.sqrt(pow(i+1, 2)+pow(j+1, 2))
t2 = time.time()
print(f"Time for method where using two nested lists: {t2 - t1}\n")

# Using the list generator
t3 = time.time()
matrix_A1 = [[1.0/np.sqrt(pow(i+1, 2)+pow(j+1, 2)) for i in range(N)] for j in range(N)]
t4 = time.time()
print(f"Time for method where using list generator: {t4 - t3}\n")

# Using fromfunction()
t5 = time.time()
matrix_A2 = np.fromfunction(function_of_filling, (N, N))
t6 = time.time()
print(f"Time for method where using fromfunction(): {t6 - t5}\n")

# Comparing the execution speed of different methods
print(f"How many times faster method with fromfunction() than method with two nested lists: {(t2 - t1)/(t6 - t5)}")
print(f"How many times faster method with fromfunction() than method using list generator: {(t4 - t3)/(t6 - t5)}")