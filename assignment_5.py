# Converted from assignment_5.ipynb
# Auto-generated Python file from Jupyter notebook

# =============================================================================
# Markdown Cell 1
# =============================================================================
# # Data Analysis and Visualization with Pandas and Matplotlib
# 
# This notebook demonstrates how to use the Pandas library for data analysis and Matplotlib for data visualization in Python.

# Code Cell 2
# ===========================================================================
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Code Cell 3
# ===========================================================================
# Load a sample dataset using pandas
df = pd.read_csv('diabetes.csv')
df.head()

# Code Cell 4
# ===========================================================================
# Basic data analysis with pandas
print('DataFrame Info:')
df.info()
print('\nSummary Statistics:')
print(df.describe())

# Code Cell 5
# ===========================================================================
# Data visualization with matplotlib
if 'Age' in df.columns:
    plt.figure(figsize=(8,5))
    plt.hist(df['Age'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()
else:
    print('No Age column found in the dataset.')

# =============================================================================
# Markdown Cell 6
# =============================================================================
# ## Advanced Data Analysis and Visualization
# 
# We will now perform deeper data analysis, including handling missing values, correlation analysis, groupby operations, and multiple types of visualizations.

# Code Cell 7
# ===========================================================================
# Handling missing values
print('Missing values in each column:')
print(df.isnull().sum())

# Fill missing values with column mean (if any)
df_filled = df.fillna(df.mean(numeric_only=True))
print('\nAny missing values left?')
print(df_filled.isnull().sum())

# Code Cell 8
# ===========================================================================
# Correlation analysis and heatmap visualization
import seaborn as sns

plt.figure(figsize=(10,8))
corr = df_filled.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix Heatmap')
plt.show()

# Code Cell 9
# ===========================================================================
# Groupby analysis and bar plot visualization

# Example: Mean of all columns grouped by 'Outcome' if present
if 'Outcome' in df_filled.columns:
    group_means = df_filled.groupby('Outcome').mean(numeric_only=True)
    print(group_means)
    group_means.plot(kind='bar', figsize=(10,6))
    plt.title('Mean Values by Outcome')
    plt.ylabel('Mean Value')
    plt.xlabel('Outcome')
    plt.legend(loc='best')
    plt.show()
else:
    print('No Outcome column found for groupby analysis.')

# Code Cell 10
# ===========================================================================
# Pairplot visualization for deeper exploration
if df_filled.shape[1] <= 10:  # Limit to avoid too many plots
    sns.pairplot(df_filled, diag_kind='kde')
    plt.suptitle('Pairplot of Features', y=1.02)
    plt.show()
else:
    print('Too many columns for pairplot. Consider selecting a subset of columns.')
