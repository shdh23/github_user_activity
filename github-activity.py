from api import get_latest_events
from display import print_event_details
from utils import get_token

def main():
    username = input("Enter GitHub username: ").strip()
    repo = input("Enter repository name: ").strip()
    token = input("Enter your GitHub token (leave blank if not required): ").strip() or None
    if not token:
        token = token = get_token() or input("Enter your GitHub token (leave blank if not required): ").strip() 
        # Load token from environment if not provided

    page = 1
    while True:
        print("started")
        events = get_latest_events(username, repo, token, events_per_page=10)
        
        if isinstance(events, str):  # Error handling
            print(events)
            break

        for event in events:
            print_event_details(event)
        
        if len(events) < 10:  # No more pages available
            print("End of events.")
            break

        user_input = input("Do you want to fetch more events? (yes/no): ").strip().lower()
        if user_input not in ['yes', 'y']:
            print("Exiting event fetch.")
            break
        
        page += 1

if __name__ == "__main__":
    main()