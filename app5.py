import pandas as pd

# Load the repositories CSV file into a DataFrame
df = pd.read_csv("repositories.csv")

# Remove rows with missing language values
df = df[df['language'].notna()]

# Find the three most popular languages by counting occurrences
most_popular_languages = df['language'].value_counts().nlargest(3)

# Print the three most popular languages and their counts
for language, count in most_popular_languages.items():
    print(f"{language}: {count}")