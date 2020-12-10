import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math
import heapq
from matplotlib.colors import LogNorm
from mpl_toolkits.mplot3d import Axes3D


# define the Fermivelocity


def fermivelocity(x, y):
    if (np.sqrt(1-(np.cos(np.pi*x)**4+np.cos(np.pi*y)**4)/(np.cos(np.pi*x)**2+np.cos(np.pi*y)**2)) == 0):
        return 1
    else:
        return np.sqrt(1-(np.cos(np.pi*x)**4+np.cos(np.pi*y)**4)/(np.cos(np.pi*x)**2+np.cos(np.pi*y)**2))


# define the DOS

def DOS(n):
    dos = 0
    for x in range(200):
        for y in range(200):
            E = 2*np.sqrt(np.cos((x/100-1)*np.pi)**2 +
                          np.cos((y/200-0.5)*np.pi)**2)
            dos = dos + 0.04/((2*np.sqrt(2)*(n-1) - E) ** 2+0.04 ** 2) + \
                0.04/((2*np.sqrt(2)*(n-1) + E) ** 2 + 0.04 ** 2)
    return dos/(40000*np.pi)


# input the electron concentration
n = input("input a concentration:")
n = float(n)
D = DOS(n)

# get the FS data
# the fermi pocket's discretization
if (n > 0.29285):
    pocket_1 = []
    X2_boundary = np.arccos(np.sqrt(2)*(1-n))/np.pi
    X1_boundary = np.arccos(np.sqrt(2)*(-1+n))/np.pi
    for x in np.linspace(X1_boundary, X2_boundary, 8):
        y = np.arccos(np.sqrt(2*(1-n)**2-np.cos(x*np.pi)**2))/np.pi
        pocket_1.append([x, y])
        # plt.scatter(x, y, alpha=0.6)
    del pocket_1[0]
    pocket_1.insert(0, [X1_boundary, 1/2])
    del pocket_1[1]
    pocket_1.append([X2_boundary, 1/2])
    pocket_2 = []
    for i in range(8):
        Coord1 = pocket_1[i]
        pocket_2.append([-Coord1[0], Coord1[1]])
        # plt.scatter(Coord[0], Coord[1], alpha=0.6)

    pocket_3 = []
    for i in range(8):
        Coord1 = pocket_1[i]
        pocket_3.append([Coord1[0], -Coord1[1]])
        # plt.scatter(Coord[0], Coord[1], alpha=0.6)

    pocket_4 = []
    for i in range(8):
        Coord1 = pocket_1[i]
        pocket_4.append([-Coord1[0], -Coord1[1]])
        # plt.scatter(Coord[0], Coord[1], alpha=0.6)
    # plt.xlabel("$k_x/\pi$")
    # plt.ylabel("$k_y/\pi$")
    # plt.xlim(-1, 1)
    # plt.ylim(-0.5, 0.5)
    # plt.title('discretization of FS')
    # plt.savefig('DFS.png', dpi=500)
    pocket_1.extend(pocket_2)
    pocket_1.extend(pocket_3)
    pocket_1.extend(pocket_4)
# the hole pocket's discretization
elif (n < 0.29285):
    pocket_1 = []
    Y_boundary = np.arccos(np.sqrt(2*(1-n)**2-1))/np.pi
    for y in np.linspace(-Y_boundary, Y_boundary, 2):
        x = np.arccos(np.sqrt(2*(1-n)**2-np.cos(y*np.pi)**2))/np.pi
        pocket_1.append([x, y])
        # plt.scatter(x, y, alpha=0.6)
    print(pocket_1)
    pocket_2 = []
    for i in range(4):
        Coord = pocket_1[i]
        pocket_2.append(Coord[0], -Coord[1])
        # plt.scatter(Coord[0], Coord[1], alpha=0.6)

    pocket_3 = []
    for i in range(4):
        Coord = pocket_1[i]
        pocket_2.append(-Coord[0], Coord[1])
        # plt.scatter(Coord[0], Coord[1], alpha=0.6)

    pocket_4 = []
    for i in range(4):
        Coord = pocket_1[i]
        pocket_4.append(-Coord[0], -Coord[1])
        # plt.scatter(Coord[0], Coord[1], alpha=0.6)
    # plt.xlabel("$k_x/\pi$")
    # plt.ylabel("$k_y/\pi$")
    # plt.xlim(-1, 1)
    # plt.ylim(-0.5, 0.5)
    # plt.title("discretization of FS")
    # plt.savefig('DFS.png', dpi=500)

    pocket_1.extend(pocket_2)
    pocket_1.extend(pocket_3)
    pocket_1.extend(pocket_4)

elif (n == 0.29285):
    print(DOS(n))


# define the area of fermisurface

# fermisurface = 0
# for i in range(59):
#    p1 = np.array(pocket_1[i])
#    p2 = np.array(pocket_1[i+1])
#    p3 = p2 - p1
#    distance = math.hypot(p3[0], p3[1])
#    fermisurface = fermisurface + 4*np.pi*distance

# define the average fermion velocity
averageFV = 0
for i in range(2):
    p1 = np.array(pocket_1[i])
    p2 = np.array(pocket_1[i+1])
    p3 = p2 - p1
    distance = math.hypot(p3[0], p3[1])
    averageFV = averageFV + distance*np.pi * 1 / \
        fermivelocity((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
averageFV = 1/averageFV

# define the magnetic susceptibility


def ms(x, y, n, z):
    if (n > 0.29285):
        chi = 0
        for i in np.linspace(-1, 1, z):
            for j in np.linspace(-0.5, 0.5, z):
                if (-2*np.sqrt(np.cos(np.pi*i)**2+np.cos(np.pi*j)**2)+2*np.sqrt(2)*(1-n) > 0):
                    chi = chi
                else:
                    chi = chi + (2*(2*np.pi)**-2)*1/(0.000001j + np.sqrt(np.cos(np.pi*(x+i))**2+np.cos(
                        np.pi*(y+j))**2)-np.sqrt(np.cos(np.pi*(i))**2+np.cos(np.pi*(j))**2))*(2/z*1/z)
        return chi


# Constructions of the Gamma Matrix and execute the iteration of RG
U = 0.2
cutoff = 1e-40
cutoff_phy = 4*np.sqrt(2)*np.exp(-1/(D*U))
print(cutoff_phy)
iteration_index = 0
GammaMatrix = np.zeros((60, 60))
min_egin = 0
print(pocket_1)
while min_egin < 1:
    for i in range(32):
        for j in range(i):
            x = pocket_1[i]
            y = pocket_1[j]
            GammaMatrix[i][j] = D*0.1**2*averageFV / \
                (np.sqrt(fermivelocity(
                    x[0], x[1])*fermivelocity(y[0], y[1]))*(ms(x[0]+y[0], x[1]+y[1], n, 600).real+D*math.log(1/cutoff)))
            GammaMatrix[j][i] = GammaMatrix[i][j]
            print(GammaMatrix[i][j])
    np.set_printoptions(precision=3) 
    np.set_printoptions(threshold=np.inf)
    A, B = np.linalg.eig(GammaMatrix)
    min_index = np.argsort(A)
    min_egin = np.abs(min(A))
    cutoff = cutoff/10
    iteration_index = iteration_index + 1
    print("iteration number of RG is %d" %(iteration_index))
    print(min_egin)


# X = []
# Y = []
# for i in range(120):
#   x = pocket_1[i]
#    X.append(x[0])
#   Y.append(x[1])
#Z = B[min_index[0]]
