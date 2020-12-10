import matplotlib.pyplot as plt
import numpy as np
X = [[0, 0.25], [0.5, 0.75]] 
Z = np.zeros((200,100))
Z[2][3] = 100
plt.imshow(Z)