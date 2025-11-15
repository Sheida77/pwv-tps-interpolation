from scipy.interpolate import griddata
import math
import numpy as np

# Load data from text files
OrthoHeight = np.loadtxt('usorth.txt', usecols=2)
latitude = np.loadtxt('usort.txt', usecols=0)
Geopotential = np.loadtxt('zsum.txt', usecols=(4))
Pressure = np.loadtxt('zsum.txt', usecols=(1))
Pressure = np.array(Pressure).reshape(12, 2997)

# Geopotential height calculation
GeopotentialHeight = Geopotential / 9.80665
GeopotentialHeight = np.array(GeopotentialHeight).reshape(12, 2997)

lattt = np.array(np.loadtxt('zsum.txt', usecols=(2))).reshape(12, 2997)
lonnn = np.array(np.loadtxt('zsum.txt', usecols=(3))).reshape(12, 2997)

# Calculate pressure based on interpolation
cordinateee = []
for i in range(2997):
    cordinateee.append(np.array([lattt[5][i], lonnn[5][i], GeopotentialHeight[5][i]]))
points = cordinateee
values = Pressure[5]
xi = np.loadtxt('usorth.txt')
Ps = []
for i in xi:
    if i[2] > min(GeopotentialHeight[5]) + 10:
        Ps.append(griddata(points, values, i, method='linear'))
    else:
        Ps.append(1000)

# Calculate ZHD (zenith hydrostatic delay)
radians = []
for i in latitude:
    radians.append(math.radians(i))
ZHD = []
for num in range(len(latitude)):
    ZHD.append(((0.0022767 * Ps[num]) / (1 - (0.00266 * np.cos(2 * 0.7349194857648396) - (0.00000028 * OrthoHeight[num])))))

print(ZHD)

# Load additional ZTD data
ZTD = np.loadtxt('sumu.txt', usecols=2)
ZTD = np.array(ZTD).reshape(len(latitude), 12)

# Calculate ZWD (zenith wet delay)
ZWD = []
for i in range(len(latitude)):
    ZWD.append(ZTD[i][6] - (ZHD[i] * 1000))

print(ZWD)
