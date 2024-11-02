import pandas as pd
from collections import Counter

# Load the users CSV file into a DataFrame
df = pd.read_csv("users.csv")

# Drop rows with missing names
df = df[df['name'].notna()]

# Extract the last word (surname) from each name, trimming whitespace
surnames = df['name'].str.split().str[-1].str.strip()

# Count the occurrences of each surname
surname_counts = Counter(surnames)

# Find the maximum occurrence count
max_count = max(surname_counts.values())

# Get all surnames that have the maximum count
most_common_surnames = sorted([surname for surname, count in surname_counts.items() if count == max_count])

# Print the most common surname(s) and the count
print(f"Most common surname(s): {','.join(most_common_surnames)}")
print(f"Number of users with the most common surname: {max_count}")