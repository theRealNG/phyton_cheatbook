import pandas as pd

# Reading a csv file
housing_2013 = pd.read_csv("Hud_2013.csv")

# Finding mean
titanic_survival["fare"].mean()

# Finding number of columns
num_columns = len(housing_2013.columns)

# Finding the index of the least element
lowest_income_county = income.iloc[income["median_income"].idxmin()]["county"]

# Returns the first 5 rows of data not counting column headers
housing_2013.head(5)

# Selecting data
red_flags = len(flags[flags['red'] == 1])
orange_flags = len(flags[flags['orange'] == 1])
red_and_orange_flags = len(flags[(flags['orange'] == 1) & (flags['red'] ==1)])

# Sorting data
pixar_movies = pixar_movies.sort(['Opening Weekend'],ascending=[True])

# Renaming a column
df.rename(columns={'$a': 'a', '$b': 'b'}, inplace=True)

# Formatting data
# the bracket notation [ ] is how we specify the the list of columns we want to select
filtered_housing_2013 = housing_2013[[ 'AGE1', 'FMR','TOTSAL' ]]

# Drop missing values
# will ignore the rows where age or body or home.dest has a missing value
new_titanic_survival = titanic_survival.dropna(subset=["age","body","home.dest"])

# calculating Median
median_age = numpy.median(titanic_survival["age"])

# calculating Mean
mean_age = titanic_survival["age"].mean()
mean_age = numpy.mean(age_list)

# calculating skew
skew_age = skew(titanic_survival["age"])

# calculating kurtosis
# kurtosis measures the shape of a distribution.
kurtosis_age = kurtosis(titanic_survival["age"])

# variance is the sum of the mean difference of all the elements by number of elements
mean_pts = nba_stats["pts"].mean()
mean_diff_values = [  val - mean_pts for val in nba_stats["pts"] ]
mean_square_diff_values = [ val**2 for val in mean_diff_values ]
point_variance = sum(mean_square_diff_values)/len(mean_square_diff_values)

stats_variance = nba_stats["pts"].var()

# standard deviation
# how far data points are from the mean is called standard deviation.
def calculate_std_deviation(col_name):
    mean_value = nba_stats[col_name].mean()
    mean_diff = [ val - mean_value for val in nba_stats[col_name] ]
    mean_sq_diff = [ val ** 2 for val in mean_diff ]
    variance = sum(mean_sq_diff)/len(mean_sq_diff)
    std_deviation = variance ** (1/2)
    return std_deviation

# how many standard deviations away from the mean
abs(value - mean)/standard_deviation

# Find the co-relation between two set of values
from scipy.stats.stats import pearsonr
co_relation_value, pvalue = pearsonr(nba_stats["fta"], nba_stats["pts"])

# finding covariance
# You can use the cov function from numpy to compute covariance.
# It returns a 2x2 matrix, though.
# cov(nba_stats["pf"], nba_stats["stl"])[0,1]
# will give the covariance between the "pf" and "stl"
cov(nba_stats["fta"], nba_stats["blk"])[0,1]

# Plot a blue line at median
plt.axvline(median, color="b")

# Plotting a line
x = [0, 1, 2, 3, 4, 5]
x = np.asarray([0, 1, 2, 3, 4, 5])
y = x + 1
plt.plot(x, y)
plt.show()

# Finding slope of a line
m = (cov(x,y)/x.var())[0,1]
# Finding the intercept
c = y.mean() - m * x.mean()


# %% Indexing %%
#.iloc works by position (row/column number)
row_4 = new_titanic_survival.iloc[4,:]

#.loc addresss row and columns by index and not by position
row_with_index_3 = new_titanic_survival.loc[3,:]
row_with_index_1100_age = new_titanic_survival.loc[1100,"age"]
row_with_index_25_survived = new_titanic_survival.loc[25,"survived"]

# Reset index
# the drop keyword argument specifies whether or not to make a dataframe column with the index values.
new_titanic_survival = titanic_survival.dropna(subset=["age","boat"])
titanic_reindexed = new_titanic_survival.reset_index(drop=True)


# %% Apply Function %%
# by default, .apply() will iterate throuh each column in a dataframe and perform a function on it
def not_null_count(col):
    col_null = pd.isnull(col)
    not_null = col[col_null == False]
    return len(not_null)

column_not_null_count = titanic_survival.apply(not_null_count)

# another example
def convert_to_ratings(col):
    if col == 'Very favorably':
        return 6
    elif col == 'Somewhat favorably':
        return 5
    elif col == 'Neither favorably nor unfavorably (neutral)':
        return 4
    elif col == 'Somewhat unfavorably':
        return 3
    elif col == 'Unfamiliar (N/A)':
        return 2
    elif col == 'Very unfavorably':
        return 1
    else:
        return col
star_wars[character] = star_wars[character].apply(convert_to_ratings)

# for applying a function on each row
def age_is_minor(row):
    age = row["age"]
    if pd.isnull(age):
        return "unknown"
    elif age >= 18:
        return "adult"
    else:
        return "minor"

age_labels = titanic_survival.apply(age_is_minor, axis=1)

# another example
def number_of_deaths(row):
    counts = row[['Death2','Death1','Death3','Death4','Death5']].value_counts()
    return counts['YES'] if 'YES' in counts else 0

true_avengers['Deaths'] = true_avengers.apply(number_of_deaths, axis=1)


# %% Pivot Tables %%
# Let's compute the survival change from 0-1 for people in each class
# The closer to one, the higher the chance people in that passenger class survived
# The "survived" column contains a 1 if the passenger survived, and a 0 if not
# The pivot_table method on a pandas dataframe will let us do this
# index specifies which column to subset data based on (in this case, we want to compute the survival percentage for each class)
# values specifies which column to subset based on the index
# The aggfunc specifies what to do with the subsets
# In this case, we split survived into 3 vectors, one for each passenger class, and take the mean of each
passenger_survival = titanic_survival.pivot_table(index="pclass", values="survived", aggfunc=np.mean)

port_stats = titanic_survival.pivot_table(index="embarked", values=["age","survived","fare"], aggfunc=np.mean)
