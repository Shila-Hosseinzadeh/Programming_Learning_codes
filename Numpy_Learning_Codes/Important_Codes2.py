import numpy as np

A = np.array(([1, 2, 3], [1, 2, 3]))
B = np.array([1,2,3])

# slicing and indexing array
print(f"A : {A}")
print(f"B : {B}")
print(f"A[0] : {A[0]}")
print(f"B[:2] : {B[:2]}")
print(f"B[:-1] : {B[:-1]}")

# change the items in array
print(f"B : {B}")
print(f"A : {A}")
B[1]=198
A[1]= 11,22,33
print(f"B[1]=198 : {B}")
print(f"A : {A}")


# attributes
print(f"type(B) : {B.dtype}")
print(f"type(A) : {A.dtype}")

print(f"shape(A) : {A.shape}")
print(f"size(B) : {B.size}")
print(f"number of dimention(B) : {B.ndim}")
print(f"number of dimention(A) : {A.ndim}")

# vector operation(+ , - ,* ,/ ,....)
A = np.array([13,22,11])
B = np.array([1,2,3])
print (f"A + B : {A+B}")

# item to item product:(Hadamard product)
A = np.array([13,22,11])
B = np.array([1,2,3])
print (f"Hadamad product of (A,B) is array: {A*B}")

# inner product (dot product)
A = np.array([13,22,11])
B = np.array([1,2,3])
print (f"inner product of(A,B) is scalar: {np.dot(A,B)}")

# broadcasting array
B = np.array([1,2,3])
print(f"B : {B}")
print(f"B + 1 : {B +1 }")

print(f"B : {B}")
print(f"B * 5 : {B * 5 }")

# Numpy methods

A = np.array(([1, 2, 3], [1, 2, 3]))
B = np.array([1,2,3])
C = np.array ([0 , np.pi/2 ,np.pi ,np.pi *3/6])
print(f"mean of(A) : {np.mean(A)}")
print(f"max of(A) : {np.max(A)}")
print(f"min of(A) : {np.min(A)}")
print(f"cos of(C) : {np.cos(C)}")
print(f"tanh of(C) : {np.tanh(C)}")
print(f"median of(C) : {np.median(C)}")
print(f"median of(B) : {np.median(B)}")
print(f"median of(A) : {np.median(A)}")
print(f"var of(B) : {np.var(B)}")
print(f"std of(B) : {np.std(B)}")

# linspace
print(f"linspace of(D) : {np.linspace(0,50,num = 3)}")
