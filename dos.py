import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
E = np.zeros((50, 100))
N = np.linspace(0, 2.0, 200)
Dos1 = []
Dos2 = []
Dos3 = []

for n in np.linspace(0, 2.0, 200):
    rho1 = 0
    for x in range(200):
        for y in range(200):
            E = 2*np.sqrt(np.cos((x/100-1)*np.pi)**2+np.cos((y/200-0.5)*np.pi)**2)
            rho1 = rho1 + 0.04/((2*np.sqrt(2)*(n-1) - E) ** 2+0.04 ** 2) + 0.04/((2*np.sqrt(2)*(n-1) + E) ** 2 + 0.04 ** 2)
    Dos1.append(rho1/(40000*np.pi))


for n in np.linspace(0, 2.0, 200):
    rho2 = 0
    for x in range(200):
        for y in range(200):
            E = 2*(np.cos((x/100-1)*np.pi)+np.cos((y/100-1)*np.pi))
            rho2 = rho2 + 0.04/((4*(n-1) - E) ** 2+0.04 ** 2) + 0.04/((4*(n-1) + E) ** 2 + 0.04 ** 2)
    Dos2.append(rho2/(40000*np.pi))


plt.plot(N, Dos1, color='red', linewidth=2, label='$\pi$-flux')
plt.plot(N, Dos2, color='blue', linewidth=2, label='0-flux')
plt.title('DOS')
plt.xlabel("n")
plt.ylabel("DOS")
plt.legend()
plt.savefig('DOS.png', dpi=500)
