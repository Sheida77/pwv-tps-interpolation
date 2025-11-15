import numpy as np
from scipy.interpolate import griddata

# Load data from text files
xii = []
for i in range(len(Ps)):
    xii.append(np.array([Ps[i], np.loadtxt('Nusort.txt', usecols=0)[i], np.loadtxt('Nusort.txt', usecols=1)[i]]))

# Perform grid interpolation for RH and temperature
cordinatee = []
for i in range(2997):
    cordinatee.append(np.array([p[5][i], lat[5][i], lon[5][i]]))

# Interpolation for RH (relative humidity)
points = cordinatee
values = r[5]
xi = xii
rhh = []
for i in xi:
    rhh.append(griddata(points, values, i, method='linear'))

# Perform grid interpolation for temperature (T)
cordinateee = []
for i in range(2997):
    cordinateee.append(np.array([lattt[5][i], lonnn[5][i], GeopotentialHeight[5][i]]))

T = np.array(np.loadtxt('tempwin.txt', usecols=(4))).reshape(12, 2997)
cordinat = []
for i in range(2997):
    cordinat.append(np.array([p[5][i], lat[5][i], lon[5][i]]))

points = cordinat
values = T[5]
xi = xii
daama = []
for i in xi:
    daama.append(griddata(points, values, i, method='linear'))

# Calculate saturation vapor pressure
e1 = []
for i in range(4):
    e1.append(6.11 * (10 ** ((7.5 * daama[i]) / (daama[i] + 273.15))))

# Calculate actual vapor pressure
es = []
for i in range(4):
    es.append(e1[i] * (rhh[i] / 100))

# Calculate water vapor density (ZWD)
zwd = []
for i in range(4):
    zwd.append(0.002277 * ((1255 / daama[i]) + 0.05) * es[i])

# Constants for the calculations
R = 461.51
k1 = 77.689
k2 = 71.295
k3 = 3.75463 * (10 ** 5)
ro = 999
mw = 18.0152
md = 28.9644

# Calculate temperature correction (Tm)
Tm = []
for i in range(4):
    Tm.append((70.2 + 0.72 * daama[i]))

# Calculate precipitable water vapor (PWV)
PI = []
for i in range(4):
    PI.append(((10 ** 6) / (((k3 / Tm[i]) + k2) * ro * R)) * 100)

# Final PWV calculation
PWV = []
for i in range(4):
    PWV.append(PI[i] * zwd[i])

# Output the calculated PWV
print(PWV)
