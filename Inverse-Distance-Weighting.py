import numpy as np
from math import dist

# Define the IDW function
def idw_interpolation(cordinate, cordinateee, values, pWv, power=2):
    # Calculate the distances between points
    distanceQ = []
    for j in range(len(cordinateee)):
        for i in range(len(cordinate)):
            distanceQ.append(1 / ((dist(cordinate[i], cordinateee[j])) ** power))
    
    # Convert distances to an array
    distance = np.array(distanceQ).reshape(len(cordinate), len(cordinateee))
    
    # Calculate weights based on distances
    up = []
    for i in range(len(distance)):
        for r in range(len(cordinateee)):
            up.append(distance[i][r] * pWv[0][r])
    
    # Convert weights to an array
    Up = np.array(up).reshape(len(cordinate), len(cordinateee))
    
    # Sum the weights for each point
    SumMulti = []
    for i in Up:
        SumMulti.append(sum(i))
    
    # Sum the distances for each point
    SumMultii = []
    for j in distance:
        SumMultii.append(sum(j))
    
    # Calculate the predicted value for each point
    k = []
    for i in range(len(cordinate)):
        k.append(SumMulti[i] / SumMultii[i])
    
    return k

# Compute the predictions
cordinate = np.loadtxt('2277.txt')  # Data points for prediction
cordinateee = np.loadtxt('usort.txt')  # Reference points for interpolation
pWv = np.loadtxt('pwvsum.txt', usecols=0)  # PWV values

# Use IDW to compute the prediction
predicted_values = idw_interpolation(cordinate, cordinateee, pWv, pWv)  # Prediction using IDW

# Print the predicted values
print(predicted_values)

# Calculate RMSE for evaluation
rms = []
pwvv = np.loadtxt('pwvsum.txt', usecols=0)  # Actual PWV values
for i in range(4):
    rms.append((predicted_values[i] - pwvv[i]) ** 2)

print('RMSE: ', np.sqrt(sum(rms) / 4))
