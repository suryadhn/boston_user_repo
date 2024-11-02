import pandas as pd

# Load the users CSV file into a DataFrame
df = pd.read_csv("users.csv")

# Find the three most common companies among all users
most_common_companies = df['company'].value_counts().nlargest(3)

# Print the companies and their counts
for company, count in most_common_companies.items():
    print(f"{company}: {count}")