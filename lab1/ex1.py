import numpy as np
import time

k = 10**6
x = np.random.random(size=k).astype(float)
y = np.random.random(size=k).astype(float)

# Used numpy
t1 = time.time()
sum_array_np = x + y
dif_array_np = x - y
dot_array_np = x * y
div_array_np = x / y
t2 = time.time()
dt1 = t2 - t1

print("Arrays for method with numpy:")
print(f"The amount:{sum_array_np}\n")
print(f"Subtraction:{dif_array_np}\n")
print(f"Multiplication:{dot_array_np}\n")
print(f"Splitting:{div_array_np}\n")

# Used python syntax and numpy
t3 = time.time()
sum_array_pt = np.zeros(k)
dif_array_pt = np.zeros(k)
dot_array_pt = np.zeros(k)
div_array_pt = np.zeros(k)

for i in range(k):
    sum_array_pt[i] = x[i] + y[i]
    dif_array_pt[i] = x[i] - y[i]
    dot_array_pt[i] = x[i] * y[i]
    div_array_pt[i] = x[i] / y[i]
t4 = time.time()
dt2 = t4 - t3

print("Arrays for method with numpy and python:")
print(f"The amount: {sum_array_pt}\n")
print(f"Subtraction: {dif_array_pt}\n")
print(f"Multiplication: {dot_array_pt}\n")
print(f"Splitting: {div_array_pt}\n")

# Used only python syntax
# Converting the original numpy arrays to a python list
x1 = x.tolist()
y1 = y.tolist()

for i in range(k):
    x1.append(x[i])
    y1.append(y[i])

t5 = time.time()
sum_array_pt1 = []
dif_array_pt1 = []
dot_array_pt1 = []
div_array_pt1 = []

for i in range(k):
    sum_array_pt1.append(x1[i] + y1[i])
    dif_array_pt1.append(x1[i] - y1[i])
    dot_array_pt1.append(x1[i] * y1[i])
    div_array_pt1.append(x1[i] / y1[i])
t6 = time.time()
dt3 = t6 - t5

print("Arrays for method python:")
print(f"The amount: {sum_array_pt1[:3]}, '...\n', {sum_array_pt1[-3:]}\n")
print(f"Subtraction: {dif_array_pt1[:3]}, '...\n', {dif_array_pt1[-3:]}\n")
print(f"Multiplication: {dot_array_pt1[:3]}, '...\n', {dot_array_pt1[-3:]}\n")
print(f"Splitting: {div_array_pt1[:3]}, '...\n', {div_array_pt1[-3:]}\n")

print(f"Time for method with numpy: {dt1}")
print(f"Time for method with numpy and python syntax: {dt2}")
print(f"Time for method with python syntax: {dt3}")

print(f"Time with numpy and python vs time with numpy: {dt2/dt1}")
print(f"Time with python vs time with numpy: {dt3/dt1}")
