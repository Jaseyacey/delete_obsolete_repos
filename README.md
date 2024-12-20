# GitHub Repository Deletion Script

A Python script to bulk delete GitHub repositories using the GitHub REST API.

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)
- GitHub Personal Access Token with `delete_repo` permissions

## Setup

1. Clone this repository or download the script
2. Install required dependencies:
   ```bash
   pip install requests
   ```
3. Create a GitHub Personal Access Token:
   - Go to GitHub Settings → Developer Settings → Personal Access Tokens → Tokens (classic)
   - Generate new token (classic)
   - Select the `delete_repo` scope
   - Copy the generated token

4. Update the script with your:
   - GitHub Personal Access Token
   - GitHub username
   - List of repositories to delete

## Usage

1. Edit the script to include your configuration:
   ```python
   token = 'YOUR_GITHUB_TOKEN'  # Replace with your token
   username = 'YOUR_USERNAME'   # Replace with your GitHub username
   repos_to_delete = ['repo1', 'repo2']  # Add repositories to delete
   ```

2. Run the script:
   ```bash
   python deleteRepo.py
   ```

## Safety Features

- The script provides status codes and error messages for failed deletions
- Each deletion requires the correct permissions
- Repository names must be explicitly listed in the `repos_to_delete` array

## Warning

⚠️ Repository deletion is permanent and cannot be undone. Use this script with caution.

## Error Handling

The script will output:
- Success messages for successfully deleted repositories
- Error codes and messages for failed deletions
- Common error codes:
  - 204: Success
  - 403: Authentication/permission error
  - 404: Repository not found

## Contributing

Feel free to submit issues and enhancement requests!

## License

[MIT](https://opensource.org/licenses/MIT)