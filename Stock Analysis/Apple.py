import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt

# Function to fetch historical stock data
def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# Function to perform linear regression and make predictions
def linear_regression_prediction(stock_data):
    # Use the 'Close' prices as the dependent variable (y)
    y = stock_data['Close'].values.reshape(-1, 1)

    # Use the index as the independent variable (x)
    x = np.arange(len(y)).reshape(-1, 1)

    # Split the data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Create a linear regression model
    model = LinearRegression()

    # Train the model
    model.fit(x_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(x_test)

    # Calculate and print the model's performance metrics
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

    # Plot the actual vs. predicted prices
    plt.scatter(x_test, y_test, color='black')
    plt.plot(x_test, y_pred, color='blue', linewidth=3)
    plt.title('Stock Price Prediction using Linear Regression')
    plt.xlabel('Index')
    plt.ylabel('Stock Price')
    plt.show()

# change these settings to see other stocks and date ranges
if __name__ == "__main__":
    ticker_symbol = 'AAPL'  # Replace with the desired stock symbol
    start_date = '2022-9-1'
    end_date = '2023-12-14'

    # Fetch historical stock data
    stock_data = get_stock_data(ticker_symbol, start_date, end_date)

    # Perform linear regression and make predictions
    linear_regression_prediction(stock_data)
