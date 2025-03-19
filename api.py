import requests
from display import print_event_details

def get_latest_events(username, repo, token, events_per_page):
    url = f"https://api.github.com/repos/{username}/{repo}/events"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        response = requests.get(url, headers=headers, params={'per_page': events_per_page})
        response.raise_for_status()
        events = response.json()

        number_of_events = len(events)
        if number_of_events == 0:
            print("No events found.")
            return []
        
        return events
    
    except requests.exceptions.HTTPError as e:
        if response.status_code == 403:
            return f"Rate limit exceeded for {username}/{repo}. Try again later."
        elif response.status_code == 404:
            return f"User '{username}' or repository '{repo}' not found."
        else:
            return f"Error fetching events for {username}/{repo}: {e}"

    except requests.exceptions.RequestException as e:
            return f"Network error: {e}"