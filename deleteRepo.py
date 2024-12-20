import requests

# Replace 'GITHUB_TOKEN_TO_DELETE_REPOS' with your GitHub token
token = 'GITHUB_TOKEN_TO_DELETE_REPOS'
headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Add the names of the repos you want to delete
repos_to_delete = ['repo1', 'repo2', 'repo3']
username = 'GITHUB_USERNAME'

for repo in repos_to_delete:
    url = f'https://api.github.com/repos/{username}/{repo}'
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f'Successfully deleted {repo}')
    else:
        print(f'Failed to delete {repo}. Status code: {response.status_code}')
        print(f'Error message: {response.text}')