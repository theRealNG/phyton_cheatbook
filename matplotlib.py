import matplotlib.pyplot as plt

# Plot a scatterplot
month = [1,1,2,2,4,5,5,7,8,10,10,11,12]
temperature = [32,15,40,35,50,55,52,80,85,60,57,45,35]
plt.scatter(month, temperature)
plt.show()
# month will be on x-axis and temperature will be on y-axis

# Plot a line chart
plt.plot( forest_fires["wind"], forest_fires["area"])
plt.show()

# Labeling the charts
plt.title("Wind speed vs fire area")
plt.xlabel('Wind speed when fire started')
plt.ylabel('Area consumed by fire')
plt.scatter( forest_fires["wind"], forest_fires["area"])
plt.show()

# Styling the chart
# available styles
print(plt.style.available)
#=> ['fivethirtyeight', 'grayscale', 'bmh', 'ggplot', 'dark_background']
plt.style.use("fivethirtyeight")
plt.scatter( forest_fires["rain"], forest_fires["area"])
plt.show()


# %% Bar Charts %%
# The pivot_table method will return a new array containing a summary of the data.
# This pivot table will have the Y position of the fire as the index, and the average area of forest burned per fire as the values.
# It will return a vector, or one dimensional array.
area_by_y = forest_fires.pivot_table(index="Y", values="area", aggfunc=numpy.mean)

# This gets the index values of the vector, in this case, the sorted y positions
y_index = area_by_y.index
plt.bar(y_index, area_by_y)
plt.show()

# This makes a similar plot for the X positions.
area_by_x = forest_fires.pivot_table(index="X", values="area", aggfunc=numpy.mean)
plt.bar(area_by_x.index, area_by_x)
plt.show()


# %% Histograms %% using pandas
recent_grads.hist(column=["Median","Sample_size"])

# another style
recent_grads["Median"].hist()
plt.show()

# customizing histogram
# Set the `layout` parameter as `(2,1)` so the graphs are displayed as 2 rows & 1 column
# Then set `grid` parameter to `False`.
recent_grads.hist(column=columns, layout=(2,1), grid=False, bins=50)


# Box and Whisker plot
# https://www.khanacademy.org/math/probability/descriptive-statistics/box-and-whisker-plots/v/reading-box-and-whisker-plots
recent_grads[['Total','Major_category']].boxplot(by='Major_category')
# rotate the lables on x-axis by 90 degrees
plt.xticks(rotation=90)


# Plotting multiple points
plt.scatter(recent_grads['Unemployment_rate'], recent_grads['P25th'], color='red')
plt.scatter(recent_grads['ShareWomen'], recent_grads['P25th'], color='blue')
plt.show()


# %% Matplotlib internals %%
# Figure is the top-level Matplotlib object

# figsize(w,h) specifies the width and height of the plotting area
fig = plt.figure(figsize=(5,7))

# add_subplot lets you add individual plots to the figure instance
# 1st param represent the row, 2nd the column number and the last param refers to the nth plot to be returned
ax = fig.add_subplot(1,1,2)

# customizing the values for x and y axis
# x axis ranges from 1 to 12
# http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes.set_xlim
ax.set_xlim([1,12])
# y axis ranges from 15 to 105
# http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes.set_ylim
ax.set_ylim([15,105])

# setting multiple attributes at once
ax.set(xlabel="Month",ylabel="Temperature",title="Year Round Temperature",xlim=[0,13],ylim=[10,110])

# setting up a scatter plot
ax.scatter(month, temperature, color="darkblue", marker="o")

# adding data to mulitiple subplots
month_2013 = [1,2,3,4,5,6,7,8,9,10,11,12]
temperature_2013 = [32,18,40,40,50,45,52,70,85,60,57,45]
month_2014 = [1,2,3,4,5,6,7,8,9,10,11,12]
temperature_2014 = [35,28,35,30,40,55,50,71,75,70,67,49]

fig = plt.figure()
ax_left = fig.add_subplot(1,2,1)
ax_left.set(title="2013", xlim=[0,13], ylim=[10,110])
ax_left.scatter(month_2013, temperature_2013, color="darkblue", marker="o")

ax_right = fig.add_subplot(1,2,2)
ax_right.set(title="2014", xlim=[0,13], ylim=[10,110])
ax_right.scatter(month_2014, temperature_2014, color="darkgreen", marker="o")

plt.show()


# %% Seaborn %%
import seaborn as sns
# http://stanford.edu/~mwaskom/software/seaborn/introduction.html
# setting label on x-axis and y-axis
sns.distplot(births['prglngth'], kde=False)
sns.axlabel('Pregnancy Length, weeks', 'Frequency')
# kde will plot kernel density estimate when true

# Setting style
sns.set_style(style='dark')

# Boxplot
births = pd.read_csv('births.csv')
sns.load_dataset
sns.boxplot(x='birthord', y='agepreg', data=births)

# pair plotting
# http://stanford.edu/~mwaskom/software/seaborn/generated/seaborn.pairplot.html#seaborn-pairplot
# Generate a pair plot for the columns agepreg, prglngth, and birthord, in that order
sns.load_dataset
sns.pairplot(data=births, vars=['agepreg','prglngth','birthord'])
plt.show()

# Plotting multiple values against profits
sns.pairplot(data=pixar_movies, x_vars='profit', y_vars=['Length', 'Opening Weekend', 'Worldwide Gross', 'Domestic Gross', 'International Gross', 'Production Budget'], hue="Oscars Won")
plt.xticks(rotation=90)
plt.show()
