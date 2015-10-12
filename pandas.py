import pandas as pd

# Reading a csv file
housing_2013 = pd.read_csv("Hud_2013.csv")

# Finding mean
titanic_survival["fare"].mean()

# Finding number of columns
num_columns = len(housing_2013.columns)

# Returns the first 5 rows of data not counting column headers
housing_2013.head(5)

# Formatting data
# the bracket notation [ ] is how we specify the the list of columns we want to select
filtered_housing_2013 = housing_2013[[ 'AGE1', 'FMR','TOTSAL' ]]

# Drop missing values
# will ignore the rows where age or body or home.dest has a missing value
new_titanic_survival = titanic_survival.dropna(subset=["age","body","home.dest"])

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
