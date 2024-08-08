import numpy as np

#escalar = np.array(42) #array de un solo elemento
tensor = np.array([[[1,2,3],[4,5,6],[7,8,9],[0,2,45]],[[1,2,3],[4,5,6],[7,8,9],[0,2,45]]])
print(tensor) #imprime la matriz
print(tensor.ndim) #imprime las dimensiones del tensor

#Agregar o eliminar dimensiones: 

vector = np.array([1,2,3],ndmin=10) #agrega 10 dimensiones
print(vector)
print(vector.ndim)

expand = np.expand_dims(np.array ([1,2,3]),axis=0) #agrega una dimension
print(expand)
print(expand.ndim)

#Elimina las dimensiones que no estás usando
print(vector, vector.ndim) #imprime el vector y el vector con sus dimensiones
vector_2 = np.squeeze(vector) #elimina las dimensiones que no estás usando con squeeze
print(vector_2, vector.ndim)
