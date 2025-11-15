from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import numpy as np

# Load data from text file
data = np.loadtxt('corD.txt')

# Split into input and output values
X = data[:, :3]
y = data[:, 3]

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Load new data for prediction
datta = np.loadtxt('ucorD.txt')
Xnew = datta[:, :3]

# Make predictions for the new data
ynew = model.predict(Xnew)

# Show the inputs and predicted outputs
for i in range(len(Xnew)):
    print("X=%s, Predicted=%s" % (Xnew[i], ynew[i]))
