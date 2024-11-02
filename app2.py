import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("users.csv")

# Filter users located in Boston
boston_users = df[df['location'].str.contains("Boston", na=False)]

# Sort Boston users by the 'created_at' date in ascending order
earliest_boston_users = boston_users.sort_values(by="created_at").head(5)

# Get the login names of the 5 earliest registered users
earliest_logins = ",".join(earliest_boston_users['login'])

print(earliest_logins)