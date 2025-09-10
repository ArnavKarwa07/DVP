# Converted from assignment_4.ipynb
# Auto-generated Python file from Jupyter notebook

# =============================================================================
# Markdown Cell 1
# =============================================================================
# # Using Pandas for Data Information
# 
# In this notebook, we will demonstrate how to use the Pandas library to get information about a dataset, such as its structure, data types, and summary statistics.

# Code Cell 2
# ===========================================================================
# Import pandas library
import pandas as pd

# Load the dataset (replace 'diabetes.csv' with your file if needed)
df = pd.read_csv('diabetes.csv')
df.head()

# Code Cell 3
# ===========================================================================
# Display basic information about the DataFrame
print('DataFrame Info:')
df.info()

print('\nSummary Statistics:')
print(df.describe())

print('\nShape of the DataFrame:')
print(df.shape)

# =============================================================================
# Markdown Cell 4
# =============================================================================
# ## Advanced Data Exploration with Pandas
# In this section, we will explore more features of pandas for data analysis, including checking for missing values, value counts, correlation, and data visualization.

# Code Cell 5
# ===========================================================================
# Check for missing values
print('Missing values in each column:')
print(df.isnull().sum())

# Value counts for a categorical column (replace 'Outcome' with your column if needed)
if 'Outcome' in df.columns:
    print('\nValue counts for Outcome:')
    print(df['Outcome'].value_counts())

# Correlation matrix
print('\nCorrelation matrix:')
print(df.corr())

# Simple data visualization using pandas and matplotlib
import matplotlib.pyplot as plt

# Histogram of all columns
df.hist(figsize=(10,8))
plt.tight_layout()
plt.show()

# Boxplot for all columns
df.plot(kind='box', subplots=True, layout=(3,3), figsize=(12,10), sharex=False, sharey=False)
plt.tight_layout()
plt.show()
