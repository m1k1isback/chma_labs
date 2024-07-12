import numpy as np

a = np.random.uniform(-5, 5, (3, 3))
print(f"Matrix A:\n {a}\n")
b = np.random.uniform(-5, 5, 3)
print(f"Vector B: {b}\n")

print(f"The determinant of the matrix A: {np.linalg.det(a)}\n")
print(f"The trace of the matrix A: {np.trace(a)}\n")
print(f"The Euclidean norm of the matrix A: {np.linalg.norm(a, 'fro')}\n")

print(f"Solving a linear system of algebraic equations of the form Ax=B: {np.linalg.solve(a, b)}\n")

print(f"Reversed matrix A:\n {np.linalg.inv(a)}\n")

# Solving the system by the inverse matrix method
print(f"The answer obtained by solving a system of equations using an inverse matrix: {np.dot(np.linalg.inv(a), b)}\n")
x = np.dot(np.linalg.inv(a), b)

if (np.linalg.solve(a, b)).all() == (np.dot(np.linalg.inv(a), b)).all():
    print("The solutions match\n")

print(f"The eigenvalue of the matrix A:\n {np.linalg.eig(a)}\n")

print(f"Scalar dot of vector x and vector b: {np.vdot(x, b)}\n")
print(f"Vector dot of vector x and vector b: {np.cross(x, b)}\n")
print(f"Outer product of vector x and vector b:\n {np.outer(x,b)})")