# GitHub Activity CLI

The **GitHub User Activity Tracker** is a Python-based command-line tool designed to fetch and display the latest events for a specified GitHub user. This uses github api
https://docs.github.com/en/rest/activity/events?apiVersion=2022-11-28. 

## Features

- **Fetch Latest Events**: Retrieve the latest events for a specified GitHub user, including commit pushes, issue comments, and pull request actions.
- **Detailed Event Information**: Display detailed information of different types of events (e.g., commits, issues, pull requests).
- **Interactive Pagination**: The tool supports paginated requests, allowing the user to fetch and display more events interactively.
- **GitHub Token Support**: Optionally, use a GitHub token for authenticated requests to avoid rate limits on the API.
- **Error Handling**: Gracefully handles errors such as invalid usernames, API failures, or rate limiting.

## Installation

**Step 1**: Clone the repository

```sh
git clone <repository_link>
cd github_user_activity
```

**Step 2**: Install dependencies

```sh
pip install -r requirements.txt
```

**Step 4**: (Optional) Add a GitHub Token

To authenticate requests and prevent rate limits:

Create a .env file in the project root.

Add your GitHub token as follows:

```sh
GITHUB_TOKEN=your_github_token_here
```

**Step 4**: Run the application

```sh
python github-activity.py
```


## File Structure
.
├── api.py                  # Handles GitHub API requests
├── display.py              # Formats and displays event details
├── github-activity.py      # Main application file
├── .env                    # Contains your GitHub token (optional)
├── requirements.txt
├── README.md


## Requirements

Python 3.8+
Requests

Reference: https://roadmap.sh/projects/task-tracker 
