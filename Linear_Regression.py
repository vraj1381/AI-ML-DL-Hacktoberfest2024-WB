from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data
X = np.array([[1], [2], [4], [3], [5]])
y = np.array([5, 7, 11, 9, 13])

# Create a linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict
predicted = model.predict([[6]])
print("Predicted value for input 6:", predicted[0])
