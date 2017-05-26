import numpy as np 
import matplotlib.pyplot as plt 
from scipy.interpolate import griddata

data = np.loadtxt("CircuitoRC.txt")
t = data[:,0]
q_t = data[:,1]

def likeli ( q_t, y_model): 
	chi_squared = (1.0 / 2.0)*np.sum(((q_t-y_model) / 1000)**2)
	return np.exp(-chi_squared) 
	
	
def modelo(x, C , tau):  ## tau = 1 / RC
	return C*(1 - np.exp(-x*tau)) 
	
C_walk = []
tau_walk = []
l_ = [] 

C_walk = np.append(C_walk, np.random.random())
tau_walk = np.append(tau_walk, np.random.random())

y_inicial = modelo(t, C_walk[0], tau_walk[0])
l_ = np.append(l_, likeli(q_t, y_inicial))



print C_walk
print tau_walk
print l_ 


sigmaQ = 100.0
sigmatau = 0.1
iteraciones = 20000
for i in range(iteraciones):
	C_prime = np.random.normal(C_walk[i], sigmaQ ) 
	tau_prime = np.random.normal(tau_walk[i], sigmatau)
	
	y_inicial = modelo(t, C_walk[i], tau_walk[i])
	y_p = modelo(t,C_prime, tau_prime)
	
	l_p = likeli(q_t, y_p)
	l_i = likeli(q_t, y_inicial)
	
	alpha = l_p / l_i
	if(alpha>= 1.0):
		C_walk = np.append(C_walk,C_prime)
		tau_walk = np.append (tau_walk, tau_prime)
		l_ = np.append(l_, l_p)
	else:
		beta = np.random.random()
		if(beta<= alpha):
			C_walk = np.append(C_walk,C_prime)
			tau_walk = np.append (tau_walk, tau_prime)
			l_ = np.append(l_, l_p)
		else:
			C_walk = np.append (C_walk, C_walk[i])
			tau_walk = np.append(tau_walk, tau_walk[i])
			l_ = np.append(l_, l_i)



tau_min = np.amin(tau_walk)
tau_max = np.amax(tau_walk)
C_min = np.amin(C_walk)
C_max = np.amax(C_walk)
grid_m, grid_b = np.mgrid[C_min:C_max:200j, tau_min:tau_max:200j]

max_likeli_id = np.argmax(l_)
mejor_C = C_walk[max_likeli_id]
mejor_tau = tau_walk[max_likeli_id]
mejor_modelo = modelo(t, mejor_C, mejor_tau)


print mejor_C
print mejor_tau 


plt.scatter(t, q_t)
plt.plot(t, mejor_modelo, label="R = 3,97  C = 9,7", color="r")
plt.legend( loc='upper left', fontsize = 'x-small')
plt.ylabel("Carga Q(t)", fontsize=12)
plt.xlabel("Tiempo", fontsize=12)
plt.title("Carga de un circuito RC , MCMC",fontsize=18)
plt.savefig("CargaCircuito.pdf")
plt.close()





count, bins, ignored =plt.hist(C_walk, 20, normed=True)
plt.title("Histograma Qmax")
plt.savefig("Histograma.pdf")
plt.close()
count, bins, ignored =plt.hist(tau_walk, 20, normed=True)
plt.title("Histograma tau")
plt.savefig("Histograma1.pdf")
plt.close()

# Este codigo fue llevado a cabo mediante el codigo realizado en 14.MonteCarloMethods/bayes_MCMC.ipynb en el repositorio de Github Uniandes, Metodos Computacionales. 


