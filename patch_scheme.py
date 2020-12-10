import numpy as np
import matplotlib.pyplot as plt
# example
step = 0.001
x = np.arange(-1, 1, step)
y = np.arange(-1/2, 1/2, step)
X, Y = np.meshgrid(x, y)
Z = 2*np.sqrt(np.cos(np.pi*X)**2+np.cos(np.pi*Y)**2)-2*np.sqrt(2)*(0.5)
contour1 = plt.contour(
    X, Y, Z, [0.0001], label='n', colors='b')

# pathches
x = []
y = []

for j in range(3):
    x.append([-0.5, -1])
    y.append([0.5, 0.5-0.5*np.tan(22.5/180*np.pi*j)])
x.append([-0.5, -1+0.5*(np.tan(45*np.pi/180)-np.tan(22.5*np.pi/180))])
y.append([0.5, 0])
x.append([-0.5, -0.5])
y.append([0.5, 0])
x.append([-0.5, -1+0.5*(np.tan(45*np.pi/180)-np.tan(22.5*np.pi/180))])
y.append([0.5, 0])
x.append([-0.5, -0.5*(np.tan(45*np.pi/180)-np.tan(22.5*np.pi/180))])
y.append([0.5, 0])
for j in range(3):
    x.append([-0.5, 0])
    y.append([0.5, 0.5-0.5*np.tan(22.5/180*np.pi*j)])

for j in range(3):
    x.append([0.5, 1])
    y.append([0.5, 0.5-0.5*np.tan(22.5/180*np.pi*j)])
x.append([0.5, 1-0.5*(np.tan(45*np.pi/180)-np.tan(22.5*np.pi/180))])
y.append([0.5, 0])
x.append([0.5, 0.5])
y.append([0.5, 0])
x.append([0.5, 1-0.5*(np.tan(45*np.pi/180)-np.tan(22.5*np.pi/180))])
y.append([0.5, 0])
x.append([0.5, 0.5*(np.tan(45*np.pi/180)-np.tan(22.5*np.pi/180))])
y.append([0.5, 0])
for j in range(3):
    x.append([0.5, 0])
    y.append([0.5, 0.5-0.5*np.tan(22.5/180*np.pi*j)])

for j in range(3):
    x.append([0.5, 1])
    y.append([-0.5, -0.5+0.5*np.tan(22.5/180*np.pi*j)])
x.append([0.5, 1-0.5*(np.tan(45*np.pi/180)-np.tan(22.5*np.pi/180))])
y.append([-0.5, 0])
x.append([0.5, 0.5])
y.append([-0.5, 0])
x.append([0.5, 1-0.5*(np.tan(45*np.pi/180)-np.tan(22.5*np.pi/180))])
y.append([-0.5, 0])
x.append([0.5, 0.5*(np.tan(45*np.pi/180)-np.tan(22.5*np.pi/180))])
y.append([-0.5, 0])
for j in range(3):
    x.append([0.5, 0])
    y.append([-0.5, -0.5+0.5*np.tan(22.5/180*np.pi*j)])

for j in range(3):
    x.append([-0.5, -1])
    y.append([-0.5, -0.5+0.5*np.tan(22.5/180*np.pi*j)])
x.append([-0.5, -1+0.5*(np.tan(45*np.pi/180)-np.tan(22.5*np.pi/180))])
y.append([-0.5, 0])
x.append([-0.5, -0.5])
y.append([-0.5, 0])
x.append([-0.5, -1+0.5*(np.tan(45*np.pi/180)-np.tan(22.5*np.pi/180))])
y.append([-0.5, 0])
x.append([-0.5, -0.5*(np.tan(45*np.pi/180)-np.tan(22.5*np.pi/180))])
y.append([-0.5, 0])
for j in range(3):
    x.append([-0.5, 0])
    y.append([-0.5, -0.5+0.5*np.tan(22.5/180*np.pi*j)])

x.append([1, -1])
y.append([0, 0])                       
x.append([0, 0])
y.append([1/2, -1/2])

for i in range(len(x)):
    plt.plot(x[i], y[i], color='r', linestyle='--', alpha=0.5)
axes = plt.gca()
axes.set_xlim([-1, 1])
axes.set_ylim([-1/2, 1/2])
# coordinate

distance = []
coord = []
for x in np.linspace(-3/4, -1/4-0.0001, 1000):
    y_line = x + 1
    y_contour = np.arccos(np.sqrt(0.5 - np.cos(x*np.pi)**2))/np.pi
    distance.append(np.abs(y_line - y_contour))
    coord.append([x, y_contour])
print(np.argmin(distance))
print(np.amin(distance))
print(coord[np.argmin(distance)])
plt.scatter(coord[np.argmin(distance)][0],
            coord[np.argmin(distance)][1], c='k', marker='x', s=90)
a = round(coord[np.argmin(distance)][0], 3)
b = round(coord[np.argmin(distance)][1], 3)
plt.text(round(coord[np.argmin(distance)][0], 2), round(coord[np.argmin(
    distance)][1], 2), (a, b), fontdict={'size': 10, 'color': 'k'})
# plot
plt.xlabel("$k_x/\pi$")
plt.ylabel("$k_y/\pi$")
plt.yticks([-0.5, 0, 0.5])
plt.xticks([-1, -0.5, 0, 0.5, 1])
plt.title('Patch Scheme of Fermi pocket')
plt.savefig('Patch_scheme_fermi.png', dpi=500)
