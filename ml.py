# Linear Regression
from scipy.stats import linregress
import numpy

slope, intercept, r_value, p_value, stderr_slope = linregress(wine_quality["density"], wine_quality["quality"])
predicted_quality = numpy.asarray([slope * x + intercept for x in wine_quality["density"]])
residuals = (wine_quality["quality"] - predicted_quality) ** 2
rss = sum(residuals)
