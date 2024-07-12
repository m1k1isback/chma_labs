import numpy as np

# Dividing the interval [1, 20] into 6 identical parts and create an array X
x = np.linspace(1, 20, 6)
print(f"Array X: {x}\n")

# Creating a deep copy of the array X
y = x.copy()
print(f"Array Y received by deep copy of the array X: {y}\n")

# Calculate sin(Y^2) and round to 3 decimal places
y = np.sin(y**2)
y = np.round(y, 3)
print(f"Array Y after exponentiation every element to sin(Y**2): {y}\n")

# Changing the shape of arrays
x = x.reshape(2, 3)
y = y.reshape(3, 2)
print(f"Array X after changing his shape to 2*3:\n {x}\n")
print(f"Array Y after changing his shape to 3*2:\n {y}\n")

# Let's perform matrix multiplication
dot_mat = np.dot(x, y)
print(f"Result of doting arrays X and Y:\n {dot_mat}\n")

# Changing the shape of array y
y = y.reshape(2, 3)
print(f"Array Y after changing his shape to 2*3:\n {y}\n")

# Combining the X and Y matrices horizontally and vertically
a = np.hstack((x, y))
b = np.vstack((x, y))
print(f"Array A received by horizontal combine arrays X and Y:\n {a}\n")
print(f"Array B received by vertical combine arrays X and Y:\n {a}\n")