import numpy as np
import matplotlib.pylab as plt


N = 10000
equis=np.loadtxt('valores.txt')
sigma=np.random.normal(0,1, size=N)
def  PDF(sigma, equis):
    return (1/(equis*np.sqrt(2*np.pi)))*np.exp((-1)*sigma**2/(2*equis**2))

#Código tomado del repositorio del profesor Jaime Forero, ejercicio 8.
lista = [np.random.random()*np.pi]
sigma_delta = 1.0

for i in range(1,N):
    propuesta  = lista[i-1] + sigma_delta * (np.random.random()-0.5)
    r = min(1,PDF(sigma,propuesta)[i]/PDF(sigma,lista[i-1])[i])
    alpha = np.random.random()
    if(alpha<r):
        lista.append(propuesta)
    else:
        lista.append(lista[i-1])
        
a=np.mean(lista)
b=np.std(lista)
x = np.linspace(0, np.pi, 10000)
#plt.plot(x, PDF(sigma,x))
plt.hist(lista, density=True, bins=35)
plt.title("Media es 9.851608281129757 y desviación es 8.50946341519285")
plt.savefig("sigma.png")
plt.show()