import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv('StudentsPerformance.csv')

# Step 2: Preview data
print(df.head())

# Step 3: Check for null values
print("Null values before handling:")
print(df.isnull().sum())

# Step 4: Handle null values
# For this dataset, there usually aren't nulls, but we can fill or drop if any
df.fillna(0, inplace=True)  # Alternatively, df.dropna(inplace=True)

# Step 5: Convert appropriate columns to int
# Columns to convert: math score, reading score, writing score
df['math score'] = df['math score'].astype(int)
df['reading score'] = df['reading score'].astype(int)
df['writing score'] = df['writing score'].astype(int)

# Step 6: Final check
print("Data types after conversion:")
print(df.dtypes)

print("Null values after handling:")
print(df.isnull().sum())
