import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("users.csv")

# Filter users located in Boston
boston_users = df[df['location'].str.contains("Boston", na=False)]

# Sort Boston users by the number of followers in descending order
top_boston_users = boston_users.sort_values(by="followers", ascending=False).head(5)

# Get the login names of the top 5 users
top_logins = ",".join(top_boston_users['login'])

print(top_logins)