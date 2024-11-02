import pandas as pd

# Load the users CSV file into a DataFrame
df = pd.read_csv("users.csv")

# Filter users located in Boston
boston_users = df[df['location'].str.contains("Boston", na=False)]

# Calculate the correlation between followers and public_repos
correlation = boston_users['followers'].corr(boston_users['public_repos'])

# Print the correlation rounded to 3 decimal places
print(f"{correlation:.3f}")