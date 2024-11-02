import pandas as pd
from scipy.stats import linregress

# Load the users CSV file into a DataFrame
df = pd.read_csv("users.csv")

# Perform linear regression with public_repos as the predictor and followers as the response
slope, intercept, r_value, p_value, std_err = linregress(df['public_repos'], df['followers'])

# Print the slope rounded to 3 decimal places
print(f"{slope:.3f}")