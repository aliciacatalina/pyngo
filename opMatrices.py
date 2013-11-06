import numpy as np

M = [[ 6, 3, 8, 3, 8],
	 [ 1, 4, 9,-1, 9],
	 [-7,-2, 7, 4,10]]

N = [[6.0,-1.0,-3.0, 2.0],
	 [8.0,-1.0, 5.0, 6.0],
	 [2.0, 2.0,-5.0,-2.0]]

O = [[1, 4],
	 [5,-8],
	 [4,-6]]

P = [1,4,8]

Q = [[10, 8, 3],
	 [-9, 1, 0]]

R = [[10, 8, 3],
	 [-9, 1, 0],
	 [ 1, 5,-3]]

#-----------------------------------------------------------
#Da la columna i de matriz
def col(mat, i):
	i=i-1
	A=[]
	for j in range(len(mat)):
		A.append(mat[j][i])
	return A

#llamada a funcion col
col(M, 5)

#------------------------------------------------------------
#Da la matriz formada por las columnas de la lista de matriz
def cols(mat, arr):
	res=[]
	for j in range(len(arr)):
		res.append (col(mat, arr[j]))
	return res

#llamada a funcion cols
cols(M, [5,4])

#------------------------------------------------------------
#Con operaciones elementales de renglon, hace 1 el elemento (i,j) y ceros arriba y abajo de el
def pivotea(mat, r, c):
	r=r-1
	c=c-1
	aux=y = [row[:] for row in mat] #aux=mat
	for j in range(len(mat[0])):
		aux[r][j] = mat[r][j]/mat[r][c]

	for j in range(len(mat)):
		if r!=j:
			a=mat[j][c]*(-1)
			for k in range(len(mat[0])):
				aux[j][k] = (aux[r][k]*a) + aux[j][k]
	return aux

#llamada a funcion pivotea
pivotea(N, 2, 2)

#------------------------------------------------------------
#Determina la posicion del renglon que da la menor razon obtenida de dividir el elemento de la 
#ultima columna entre el correspondiente de la columna i
def mrazon(mat, col):
	col=col-1
	ultima=len(mat[0])-1
	pos=1 #posicion donde esta la menor razon
	menor=mat[0][ultima]/mat[0][col]
	for j in range(len(mat)):
		aux= mat[j][ultima]/mat[j][col]
		if aux<menor:
			menor=aux
			pos=j+1
	return pos

#llamada a funcion mrazon
mrazon(N, 3)

#---------------------------------------------------------
#multiplicacion de matrices (N de cols = N de ren)
def multiplica(m1, m2):
	A = np.matrix(m1)
	B = np.matrix(m2)
	return A*B

#llamada a funcion multiplica
multiplica(O, Q)

#---------------------------------------------------------
#inversa de matriz (tiene que ser una matriz cuadrada)
def inversa(mat):
	A = np.matrix(mat)
	return A.I

#llamada a funcion
inversa(R)

#---------------------------------------------------------
#transpuesta de matriz
def transpuesta(mat):
	A = np.matrix(mat)
	return A.T

#llamada a funcion
transpuesta(Q)

#---------------------------------------------------------
#resolver sistema de ecuaciones
def solve(mat, arr):
	A = np.array(mat)
	B = np.array(arr)
	return np.linalg.solve(A, B)

#llamada a funcion
solve(R, P)

#---------------------------------------------------------
#suma de matrices
def suma(mat1, mat2):
	A = np.matrix(mat1)
	B = np.matrix(mat2)
	return A+B

#llamada a funcion
suma(R, R)

#---------------------------------------------------------
#resta de matrices
def resta(mat1, mat2):
	A = np.matrix(mat1)
	B = np.matrix(mat2)
	return A-B

#llamada a funcion
resta(R, R)

#---------------------------------------------------------
#generar matriz identidad
def identidad(size):
	return np.identity(size)

#llamada a funcion
print identidad(3)
