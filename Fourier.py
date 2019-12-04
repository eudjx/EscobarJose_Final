import numpy as np
import matplotlib.pylab as plt

sol=np.loadtxt('monthrg.dat')

#Código para calcular la transformadad de Fourier tomado de https://jakevdp.github.io/blog/2013/08/28/understanding-the-fft/           
def Fou(x):

    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

F=Fou(sol[:,4][3480:4632])


n=1151
T=2*np.pi
h=T/n
t=np.linspace(0, (n-1)*h, n)
plt.semilogy(np.linspace(0,len(F)-1, len(F)), np.abs(F/len(F)))
plt.savefig("solar.png")
plt.show()