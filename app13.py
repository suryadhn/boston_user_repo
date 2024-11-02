import pandas as pd
from scipy.stats import linregress  # Import linregress

# Load the users CSV file into a DataFrame
df = pd.read_csv("users.csv")

# Remove users without a bio
df = df[df['bio'].notna()]

# Count the number of words in the bio (split by whitespace)
df['bio_word_count'] = df['bio'].str.split().str.len()

# Perform linear regression with bio_word_count as the predictor and followers as the response
slope, intercept, r_value, p_value, std_err = linregress(df['bio_word_count'], df['followers'])

# Print the slope rounded to 3 decimal places
print(f"{slope:.3f}")