
import numpy as np
import matplotlib.pyplot as plt

step = 0.001
x = np.arange(-1, 1, step)
y = np.arange(-1/2, 1/2, step)
X, Y = np.meshgrid(x, y)
Z = -2*np.sqrt(np.cos(np.pi*X)**2+np.cos(np.pi*Y)**2)+2*np.sqrt(2)*(0.70715)
R = -2*np.sqrt(np.cos(np.pi*X)**2+np.cos(np.pi*Y)**2)+2*np.sqrt(2)*(0.2)
W = -2*np.sqrt(np.cos(np.pi*X)**2+np.cos(np.pi*Y)**2)+2*np.sqrt(2)*(0.5)
V = -2*np.sqrt(np.cos(np.pi*X)**2+np.cos(np.pi*Y)**2)+2*np.sqrt(2)*(0.8)
U = -2*np.sqrt(np.cos(np.pi*X)**2+np.cos(np.pi*Y)**2)+2*np.sqrt(2)*(0.9)
plt.contourf(X, Y, Z)
# 画等高线
plt.contour(X, Y, Z)
plt.show()
contour1 = plt.contour(X, Y, Z, [0], label='list1', colors='k')
contour2 = plt.contour(X, Y, R, [-0.0001], colors='red')
contour3 = plt.contour(X, Y, W, [-0.0001], colors='red')
contour4 = plt.contour(X, Y, V, [0], colors='red')
contour5 = plt.contour(X, Y, U, [0], colors='red')
plt.xlabel("$k_x/\pi$")
plt.ylabel("$k_y/\pi$")
plt.title('FS at different doping')
plt.savefig('Fermisurface.png', dpi=500)
