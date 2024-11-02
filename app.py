import requests
import pandas as pd
import logging
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Setup logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# GitHub API endpoint and headers
GITHUB_API_URL = "https://api.github.com"
TOKEN = 'YOUR_SECRET_TOKEN'  # Replace with your token
HEADERS = {'Authorization': f'token {TOKEN}'}

# Setup session with retry strategy
session = requests.Session()
retry_strategy = Retry(
    total=5,               # Total retry attempts
    backoff_factor=1,      # Exponential backoff factor
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["HEAD", "GET", "OPTIONS"]  # Use 'allowed_methods' instead of 'method_whitelist'
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("https://", adapter)

def fetch_boston_users():
    """Fetch users from Boston with over 100 followers using GitHub API, handling pagination."""
    logging.info("Fetching users from Boston with over 100 followers...")
    users = []
    query = "location:boston followers:>100"
    page = 1

    while True:
        url = f"{GITHUB_API_URL}/search/users?q={query}&per_page=100&page={page}"
        response = session.get(url, headers=HEADERS)
        if response.status_code != 200:
            logging.error(f"Error fetching users: {response.status_code}")
            break

        data = response.json()
        if 'items' not in data or len(data['items']) == 0:
            break  # No more users to fetch

        logging.debug(f"Page {page}: Found {len(data['items'])} users.")
        # For each user returned in search results, fetch user details
        for user in data['items']:
            user_info = fetch_user_details(user['url'])
            if user_info:
                users.append(user_info)

        # Increment page for next set of users
        page += 1
        time.sleep(1)  # Pause to avoid hitting rate limits

    return users

def fetch_user_details(user_url):
    """Fetch detailed information for a specific user."""
    logging.debug(f"Fetching details for user URL: {user_url}")
    response = session.get(user_url, headers=HEADERS)
    if response.status_code != 200:
        logging.error(f"Error fetching user details: {response.status_code}")
        return None

    user_data = response.json()
    return {
        'login': user_data['login'],
        'name': user_data.get('name', ''),
        'company': clean_company(user_data.get('company')),
        'location': user_data.get('location', ''),
        'email': user_data.get('email', ''),
        'hireable': user_data.get('hireable', False),
        'bio': user_data.get('bio', ''),
        'public_repos': user_data['public_repos'],
        'followers': user_data['followers'],
        'following': user_data['following'],
        'created_at': user_data['created_at']
    }

def clean_company(company):
    """Clean up the company name by removing @ and trimming."""
    if company:
        clean_name = company.strip().lstrip('@').upper()
        logging.debug(f"Cleaned company name: {clean_name}")
        return clean_name
    return ''

def fetch_user_repositories(repos_url):
    """Fetch the repositories for a specific user."""
    logging.debug(f"Fetching repositories from: {repos_url}")
    repos = []
    response = session.get(repos_url, headers=HEADERS)
    if response.status_code != 200:
        logging.error(f"Error fetching repositories: {response.status_code}")
        return repos
    
    repo_data = response.json()
    logging.debug(f"Found {len(repo_data)} repositories.")

    for repo in repo_data[:500]:  # Limit to 500 most recent repos
        repos.append({
            'login': repo['owner']['login'],
            'full_name': repo['full_name'],
            'created_at': repo['created_at'],
            'stargazers_count': repo['stargazers_count'],
            'watchers_count': repo['watchers_count'],
            'language': repo.get('language', ''),
            'has_projects': repo['has_projects'],
            'has_wiki': repo['has_wiki'],
            'license_name': repo['license']['name'] if repo.get('license') else ''
        })

    return repos

def write_csv_with_pandas(filename, dataframe):
    """Write DataFrame to CSV using Pandas."""
    logging.info(f"Writing data to {filename}...")
    dataframe.to_csv(filename, index=False)
    logging.info(f"Finished writing {filename}.")

def main():
    # Step 1: Fetch Users with pagination
    users = fetch_boston_users()

    # Step 2: Write users.csv using Pandas
    if users:
        users_df = pd.DataFrame(users)
        write_csv_with_pandas('users.csv', users_df)
    else:
        logging.warning("No users data to write.")

    # Step 3: Fetch repositories and write repositories.csv using Pandas
    all_repos = []
    for user in users:
        repos = fetch_user_repositories(f"{GITHUB_API_URL}/users/{user['login']}/repos")
        if repos:
            all_repos.extend(repos)

    if all_repos:
        repos_df = pd.DataFrame(all_repos)
        write_csv_with_pandas('repositories.csv', repos_df)
    else:
        logging.warning("No repositories data to write.")

if __name__ == "__main__":
    main()