# this will predict what the 6th X point would be based on the values of Y.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample data
x = np.array([[1], [2], [3], [4], [5]])  # Input features (independent variables)
y = np.array([2, 4, 5, 4, 5])           # Target values (dependent variable)

# Create and fit the linear regression model
model = LinearRegression()
model.fit(x, y)

# Make predictions about what the 6th point of X would be
X_new = np.array([[6]])  # New data point to predict
predicted_y = model.predict(X_new)

# Display the model's coefficients and intercept
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# Plot the data points and the regression line
plt.scatter(x, y, label='Data points')
plt.plot(x, model.predict(x), color='red', label='Regression line')
plt.scatter(X_new, predicted_y, color='green', label='Predicted value')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()