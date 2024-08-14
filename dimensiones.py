import numpy as np
<<<<<<< HEAD
#Cero dimensiones
scalar = np.array(42)
print(scalar)
print(scalar.ndim)
#Una dimensión
vector = np.array([1,2,3])
print(vector)
print(vector.ndim)
#Dos dimensiones 
matriz = np.array([[1,2,3],[4,5,6]])
print(matriz) #imprime la matriz
print(matriz.ndim)
#Más de dos dimensiones
tensor = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(tensor)
print(tensor.ndim)
#Agregar o eliminar dimensiones
vector = np.array([1,2,3],ndmin=10)
print(vector)
print(vector.ndim)
#Expandir
expand = np.expand_dims(np.array([1,2,3]),axis=0)
print(expand)
print(expand.ndim)
#Eliminar dimensiones que no estás usando
print(vector, vector.ndim)
vector_2 = np.squeeze(vector)
print(vector_2, vector.ndim)
#new_item para crear archivos desde powershell
=======

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
>>>>>>> origin/main
