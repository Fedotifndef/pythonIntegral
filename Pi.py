import numpy as np

nTrials = int(10E4)
radius = 1
nInside = 0

XrandCoords = np.random.default_rng().uniform(-1,1, (nTrials))
YrandCoords = np.random.default_rng().uniform(-1,1, (nTrials))

for i in range(nTrials):
    x = XrandCoords[i]
    y = YrandCoords[i]

    if x**2+y**2<=radius**2:
        nInside = nInside + 1

area = 4*nInside/nTrials
print("Value of Pi: ", area)