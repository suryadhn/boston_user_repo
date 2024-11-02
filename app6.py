import pandas as pd

# Load the users and repositories CSV files into DataFrames
users_df = pd.read_csv("users.csv")
repos_df = pd.read_csv("repositories.csv")

# Filter for users who joined after 2020
users_after_2020 = users_df[pd.to_datetime(users_df['created_at']) > '2020-12-31']

# Get the logins of users who joined after 2020
logins_after_2020 = users_after_2020['login']

# Filter the repositories to include only those belonging to users who joined after 2020
filtered_repos = repos_df[repos_df['login'].isin(logins_after_2020)]

# Remove rows with missing language values
filtered_repos = filtered_repos[filtered_repos['language'].notna()]

# Count the occurrences of each language
language_counts = filtered_repos['language'].value_counts()

# Get the second most popular language
second_most_popular_language = language_counts.index[1]

print(second_most_popular_language)