import numpy as np #libreria numpy 
lista = np.arange(0,10) #crea un arreglo de 0 a 10
lista = np.arange(0,20) #0 es el dato inicial, 20 es el dato de stop
lista = np.arange(0,20,2) #0 es el dato inicial, 20 es el dato de stop, 2 es el dato de step 
lista = np.zeros(3) #crea un array de 3 ceros
lista = np.zeros((10,10)) #crea un array de 10x10 de ceros
lista = np.ones((10,5)) #crea un array de 10x5 de unos
lista = np.linspace(0,10,10)
lista = np.linspace(0,10,100)
lista = np.eye(4)
lista = np.random.rand()
lista = np.random.rand(4)
lista = np.random.rand(4,4)
lista = np.random.randint(1,15)
lista = np.random.randint(1,100,(10,10))
print(lista) #imprime la lista

