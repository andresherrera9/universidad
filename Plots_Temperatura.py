import numpy as np
import matplotlib.pyplot as plt 

data_0 = np.loadtxt('t_0.txt')  # Se obtienen los resultados del codigo realizado en C 
data_1 = np.loadtxt('t_1.txt')
data_2 = np.loadtxt('t_2.txt')


A = data_0
plt.figure(1)
plt.imshow(A, interpolation='nearest')
plt.grid(True)
plt.show()              #Esta manera permite visualizar los valores de una matriz con diferentes colores

B = data_0
plt.figure(1)
plt.imshow(A, interpolation='nearest')
plt.grid(True)
plt.show()

B = data_1
plt.figure(1)
plt.imshow(A, interpolation='nearest')
plt.grid(True)
plt.show()
