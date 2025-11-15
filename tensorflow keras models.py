from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot

# Load dataset
data = np.loadtxt('corD.txt')

# Split into input and output values
X = data[:, :3]
y = data[:, 3]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.67)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# Create the model
model = Sequential()
model.add(Dense(12, input_dim=3, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1))

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Fit the model
model.fit(X_train, y_train, epochs=200, batch_size=10, verbose=0)

# Make predictions on the test data
yhat = model.predict(X_test, verbose=0)

# Calculate the average error in the predictions
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_test, yhat)
print('MAE: %.3f' % mae)

# Load new data for prediction
datta = np.loadtxt('ucorD.txt')
Xnew = datta[:, :3]

# Make predictions for the new data
ynew = model.predict(Xnew)

# Print predictions for the new data
for i in range(len(Xnew)):
    print("X=%s, Predicted=%s" % (Xnew[i], ynew[i]))
