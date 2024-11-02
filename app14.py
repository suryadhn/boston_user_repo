import pandas as pd

# Load the repositories CSV file into a DataFrame
repos_df = pd.read_csv("repositories.csv")

# Convert 'created_at' to datetime format
repos_df['created_at'] = pd.to_datetime(repos_df['created_at'])

# Step 1: Filter for repositories created on weekends (Saturday: 5, Sunday: 6)
weekend_repos = repos_df[repos_df['created_at'].dt.dayofweek.isin([5, 6])]

# Diagnostic check: Print the number of weekend repos and a sample
print("Total weekend repos:", len(weekend_repos))
print("Sample of weekend repos:\n", weekend_repos[['login', 'created_at']].head())

# Step 2: Count the number of repositories created by each user on weekends
weekend_user_counts = weekend_repos['login'].value_counts()

# Diagnostic check: Print the login counts to inspect the counts after grouping
print("Weekend repository counts per user:\n", weekend_user_counts)

# Step 3: Get the top 5 users by count
top_5_counts = weekend_user_counts.nlargest(5)

# Find the minimum count in this top 5 group to capture any ties
min_count_in_top_5 = top_5_counts.min()

# Step 4: Include all users with counts greater than or equal to this minimum count
all_top_users = weekend_user_counts[weekend_user_counts >= min_count_in_top_5]

# Diagnostic check: Print all users with counts in the top 5 range
print("All users with counts in the top 5 range:\n", all_top_users)

# Step 5: Sort these users alphabetically for consistent ordering
final_top_users_sorted = all_top_users.sort_index()

# Step 6: Join the user logins into a comma-separated string
top_users_logins = ','.join(final_top_users_sorted.index)

# Print the final result
print("Final Top 5 users' logins including ties:", top_users_logins)