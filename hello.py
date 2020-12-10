U = 0.2
cutoff = 0.1
cutoff_phy = 4*np.sqrt(2)*np.exp(-1/(D*U))
print("Physical energy scale is %d" %(cutoff_phy))
iteration_index = 0
GammaMatrix = np.zeros((120, 120))
min_egin = 0
while min_egin < 1:
    for i in range(120):
        for j in range(i+1):
            x = pocket_1[i]
            y = pocket_1[j]
            GammaMatrix[i][j] = D*0.1**2*averageFV / \
                (np.sqrt(fermivelocity(
                    x[0], x[1])*fermivelocity(y[0], y[1]))*(ms(x[0]+y[0], x[1]+y[1], n)+D*math.log(1/cutoff)))
            GammaMatrix[j][i] = GammaMatrix[i][j]
    A, B = np.linalg.eig(GammaMatrix)
    min_index = np.argsort(A)
    min_egin = np.abs(min(A))
    cutoff = cutoff/10
    iteration_index = iteration_index + 1
    print("iteration number of RG is %d" %(iteration_index))
    print(min_egin)

U = 0.2
cutoff = 0.1
cutoff_phy = 4*np.sqrt(2)*np.exp(-1/(D*U))
print(cutoff_phy)
iteration_index = 0
GammaMatrix = np.zeros((60, 60))
min_egin = 0
while min_egin < 1:
    for i in range(8):
        for j in range(i+1):
            x = pocket_1[i]
            y = pocket_1[j]
            GammaMatrix[i][j] = D*0.1**2*averageFV / \
                (np.sqrt(fermivelocity(
                    x[0], x[1])*fermivelocity(y[0], y[1]))*(ms(x[0]+y[0], x[1]+y[1], n, 600).real+D*math.log(1/cutoff)))
            GammaMatrix[j][i] = GammaMatrix[i][j]
            print(GammaMatrix[i][j])
    A, B = np.linalg.eig(GammaMatrix)
    min_index = np.argsort(A)
    min_egin = np.abs(min(A))
    cutoff = cutoff/10
    iteration_index = iteration_index + 1
    print("iteration number of RG is %d" %(iteration_index))
    print(min_egin)