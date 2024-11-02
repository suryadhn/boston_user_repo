import pandas as pd

# Load the users CSV file into a DataFrame
df = pd.read_csv("users.csv")

# Calculate leader_strength
df['leader_strength'] = df['followers'] / (1 + df['following'])

# Sort users by leader_strength in descending order and get the top 5
top_leaders = df.sort_values(by='leader_strength', ascending=False).head(5)

# Get the login names of the top 5 users
top_logins = ",".join(top_leaders['login'])

print(top_logins)