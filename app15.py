import pandas as pd

# Load the users CSV file into a DataFrame
df = pd.read_csv("users.csv")

# Calculate the fraction of hireable users with email addresses
hireable_with_email = df[(df['hireable'] == True) & (df['email'].notna())].shape[0]
total_hireable = df[df['hireable'] == True].shape[0]
fraction_hireable_with_email = hireable_with_email / total_hireable if total_hireable > 0 else 0

# Calculate the fraction of non-hireable users (False or missing hireable) with email addresses
non_hireable_with_email = df[(df['hireable'] != True) & (df['email'].notna())].shape[0]
total_non_hireable = df[df['hireable'] != True].shape[0]
fraction_non_hireable_with_email = non_hireable_with_email / total_non_hireable if total_non_hireable > 0 else 0

# Calculate the difference
difference = fraction_hireable_with_email - fraction_non_hireable_with_email

# Print the result rounded to 3 decimal places
print(f"{difference:.3f}")