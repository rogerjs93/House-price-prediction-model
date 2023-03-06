from sklearn.linear_model import LinearRegression

# Define the training data
X_train = [[1000], [1500], [2000], [2500], [3000]]
y_train = [50000, 75000, 100000, 125000, 150000]

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Use the model to predict the price of a 1800 sqft house
price = model.predict([[1800]])

# Print the predicted price
print("The predicted price of a 1800 sqft house is $", round(price[0]))
