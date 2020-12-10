import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import matplotlib.cm as cm
import numpy as np

X = np.arange(-np.pi, np.pi, 0.001)
Z = np.sqrt(np.cos(X)**2)
plt.plot(X,Z)
plt.show()