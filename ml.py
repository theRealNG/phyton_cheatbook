# Linear Regression
from scipy.stats import linregress
import numpy

slope, intercept, r_value, p_value, stderr_slope = linregress(wine_quality["density"], wine_quality["quality"])
predicted_quality = numpy.asarray([slope * x + intercept for x in wine_quality["density"]])
residuals = (wine_quality["quality"] - predicted_quality) ** 2
rss = sum(residuals)

# creating a matrix
matrix = np.asarray([
    [2, 1, 25],
    [3, 2, 40]
    ], dtype=np.float32)

# operations on a matrix row
matrix[1] -= 3 * matrix[0]

# swapping rows
matrix[[2,3]] = matrix[[3,2]]


## Linear Regression
# Import the linear regression class
from sklearn.linear_model import LinearRegression

# Initialize the linear regression class.
regressor = LinearRegression()

# We're using 'value' as a predictor, and making predictions for 'next_day'.
# The predictors need to be in a dataframe.
# We pass in a list when we select predictor columns from "sp500" to force pandas not to generate a series.
predictors = sp500[["value"]]
to_predict = sp500["next_day"]

# Train the linear regression model on our dataset.
regressor.fit(predictors, to_predict)

# Generate a list of predictions with our trained linear regression model
next_day_predictions = regressor.predict(test[['value']])

# Calculating error
#square_error = [ (val - next_day_predictions[index]) ** 2 for index,val in enumerate(test['next_day'])]
square_error = (test['next_day'] - next_day_predictions) ** 2
# mean squared error
mse = sum(squared_error)/len(test)

# plotting the fit
plt.scatter(test["value"], test["next_day"])
plt.plot(test["value"], next_day_predictions)
plt.show()
