import pandas as pd

# Load the users CSV file into a DataFrame
df = pd.read_csv("users.csv")

# Fill NaN values in 'hireable' with False and convert to boolean
df['hireable'] = df['hireable'].fillna(False).astype(bool)

# Calculate the average following for hireable users
average_hireable = df[df['hireable'] == True]['following'].mean()

# Calculate the average following for non-hireable users
average_non_hireable = df[df['hireable'] == False]['following'].mean()

# Calculate the difference between averages
difference = average_hireable - average_non_hireable

# Print the result rounded to 3 decimal places
print(f"{difference:.3f}")