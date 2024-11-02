import pandas as pd

# Load the repositories CSV file into a DataFrame
repos_df = pd.read_csv("repositories.csv")

# Remove rows with missing values in the language or stargazers_count columns
repos_df = repos_df.dropna(subset=['language', 'stargazers_count'])

# Group by language and calculate the average number of stars per repository
average_stars_per_language = repos_df.groupby('language')['stargazers_count'].mean()

# Find the language with the highest average number of stars
highest_avg_stars_language = average_stars_per_language.idxmax()
highest_avg_stars = average_stars_per_language.max()

print(f"The language with the highest average number of stars per repository is {highest_avg_stars_language} with an average of {highest_avg_stars:.2f} stars.")