import pandas as pd

# Load the repositories CSV file into a DataFrame
df = pd.read_csv("repositories.csv")

# Remove rows with missing license names
df = df[df['license_name'].notna()]

# Find the 3 most popular licenses by counting occurrences
top_licenses = df['license_name'].value_counts().head(3).index.tolist()

# Format the output as a comma-separated string
top_licenses_str = ",".join(top_licenses)

print(top_licenses_str)