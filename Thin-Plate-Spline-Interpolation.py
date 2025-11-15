import math
import numpy as np
from scipy.interpolate import interp1d
from math import dist

# Load data from text files
ZTD = np.loadtxt('27.txt', usecols=2)
PressureT = np.loadtxt('tsum.txt', usecols=1)
Temperature = np.loadtxt('tsum.txt', usecols=4)
time = np.loadtxt('tsum.txt', usecols=0)
Time = time - 1048128
OrthoHeight = np.loadtxt('277.txt', usecols=3)
latitude = np.loadtxt('277.txt', usecols=1)
Geopotential = np.loadtxt('zsum.txt', usecols=(4))
Pressure = np.loadtxt('zsum.txt', usecols=(1))
GeopotentialHeight = Geopotential / 9.80665

# Interpolation to calculate pressure based on geophysical data
Ps = []
for i in OrthoHeight:
    if i > 150:
        X = GeopotentialHeight
        Y = Pressure
        interpolate_x = i
        Pressure_interp = interp1d(X, Y)
        Ps.append(Pressure_interp(interpolate_x))
    else:
        Ps.append(1000)

# Calculate Zenith Hydrostatic Delay (ZHD)
ZHD = []
for num in range(25):
    ZHD.append(((0.002277 * Ps[num]) / (1 - (0.00266 * np.cos(2 * latitude[num]) - 0.00000028 * OrthoHeight[num]))))

# Calculate Zenith Wet Delay (ZWD)
ZTD = np.array(ZTD).reshape(25, 12)
ZWD = []
for i in range(25):
    ZWD.append(ZTD[i] - ZHD[i])

# Reshape and interpolate temperature and pressure data
timee = np.array(Time).reshape(12, 2997)
Temperaturee = np.array(Temperature).reshape(12, 2997)
Pressuree = np.array(PressureT).reshape(12, 2997)

Ts = []
for i in range(12):
    X = Pressuree[i]
    Y = Temperaturee[i]
    interpolate_x = Ps
    Temperature_interp = interp1d(X, Y)
    Ts.append(Temperature_interp(interpolate_x))

# Distance-based calculations
distanceQ = []
for i in range(len(cordinatee)):
    for j in range(len(cordinate)):
        distanceQ.append(dist(cordinate[i], cordinatee[j]))

uQ = []
for i in range(len(cordinatee) * len(cordinate)):
    uQ.append(((distanceQ[i] ** 2 - 2204107818.703857 ** 2) ** 2) * (math.log((math.sqrt(distanceQ[i] ** 2 + 2204107818.703857 ** 2)))))

U = np.array(uQ).reshape(len(cordinatee), len(cordinate))

multi = []
for i in range(len(cordinatee)):
    for r in range(len(cordinate)):
        multi.append(X[11][r] * U[i][r])

sumMulti = []
for i in multi:
    sumMulti.append(sum(i))

# Final calculation of the predicted values (tps)
tps = []
for j in range(len(cordinatee)):
    tps.append(X[11][19] + X[11][20] * corX[j] + X[11][21] * corY[j] + X[11][22] * corZ[j] + sumMulti[j])

# Optionally check negative values in tps
for i in tps:
    if i < 0:
        print(i)

# Calculate RMSE (Root Mean Square Error) between predicted and actual values
pwvv = np.loadtxt('pwvsum.txt', usecols=0)
rms = []
for i in range(4):
    rms.append((tps[i] - pwvv[i]) ** 2)

print(math.sqrt((sum(rms)) / 4))

# Distance-based calculations for IDW (Inverse Distance Weighting)
distancew = []
for j in range(len(cordinatee)):
    for i in range(len(cordinate)):
        distancew.append(1 / ((dist(cordinate[i], cordinatee[j])) ** 2))

distance = np.array(distancew).reshape(len(cordinatee), len(cordinate))

up = []
for i in distance:
    for r in range(len(cordinate)):
        up.append(i[r] * pWv[11][r])

Up = np.array(up).reshape(len(cordinatee), len(cordinate))

SumMulti = []
for i in Up:
    SumMulti.append(sum(i))

SumMultii = []
for j in distance:
    SumMultii.append(sum(j))

k = []
for i in range(len(cordinatee)):
    k.append(SumMulti[i] / SumMultii[i])

# Calculate RMSE for IDW predictions
rmss = []
for i in range(4):
    rmss.append((k[i] - pwvv[i]) ** 2)

print(math.sqrt((sum(rmss)) / 4))
