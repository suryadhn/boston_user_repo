import pandas as pd

# Load the repositories CSV file into a DataFrame
df = pd.read_csv("repositories.csv")

# Convert 'has_projects' and 'has_wiki' to binary (1 for True, 0 for False)
# Here we also explicitly check if the columns have any NaN values that need handling
df['has_projects'] = df['has_projects'].fillna(False).astype(bool).astype(int)
df['has_wiki'] = df['has_wiki'].fillna(False).astype(bool).astype(int)

# Verify that the columns are binary by printing unique values
print("Unique values in 'has_projects':", df['has_projects'].value_counts())
print("Unique values in 'has_wiki':", df['has_wiki'].value_counts())

# Calculate the correlation between has_projects and has_wiki
correlation = df['has_projects'].corr(df['has_wiki'])

# Print the correlation rounded to 3 decimal places
print(f"{correlation:.3f}")
