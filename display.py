def print_commit_comment_event(event):
    repo_name = event["repo"]["name"]
    print(f"- :memo: Commented on a commit in {repo_name}")

def print_push_event(event):
    repo_name = event["repo"]["name"]
    pusher_name = event["actor"]["login"]
    print(f"- :arrow_right: {pusher_name} pushed to {repo_name}")

def print_issue_comment_event(event):
    repo_name = event["repo"]["name"]
    issue_number = event["payload"]["issue"]["number"]
    commenter_name = event["actor"]["login"]
    print(f"- :speech_balloon: {commenter_name} commented on issue #{issue_number} in {repo_name}")

def print_issue_event(event):
    repo_name = event["repo"]["name"]
    issue_number = event["payload"].get("issue", {}).get("number", "N/A")
    action = event["payload"]["action"]
    actor_name = event["actor"]["login"]
    print(f"- :ticket: {actor_name} {action} issue #{issue_number} in {repo_name}")

def print_pull_request_event(event):
    repo_name = event["repo"]["name"]
    pull_request_number = event["payload"]["pull_request"]["number"]
    action = event["payload"]["action"]
    actor_name = event["actor"]["login"]
    print(f"- :octocat: {actor_name} {action} pull request #{pull_request_number} in {repo_name}")

def print_pull_request_review_event(event):
    repo_name = event["repo"]["name"]
    pull_request_number = event["payload"]["pull_request"]["number"]
    action = event["payload"]["action"]
    reviewer_name = event["actor"]["login"]
    print(f"- :mag: {reviewer_name} {action} review on pull request #{pull_request_number} in {repo_name}")

def print_pull_request_review_comment_event(event):
    repo_name = event["repo"]["name"]
    pull_request_number = event["payload"]["pull_request"]["number"]
    action = event["payload"]["action"]
    commenter_name = event["actor"]["login"]
    print(f"- :speech_balloon: {commenter_name} {action} comment on pull request #{pull_request_number} in {repo_name}")

def print_release_event(event):
    repo_name = event["repo"]["name"]
    release_tag = event["payload"]["release"]["tag_name"]
    action = event["payload"]["action"]
    actor_name = event["actor"]["login"]
    print(f"- :rocket: {actor_name} {action} release {release_tag} in {repo_name}")

def print_create_event(event):
    repo_name = event["repo"]["name"]
    ref_type = event["payload"].get("ref_type", "unknown")
    ref_name = event["payload"].get("ref", "unknown")
    actor_name = event["actor"]["login"]
    print(f"- :sparkles: {actor_name} created a {ref_type} '{ref_name}' in {repo_name}")

def print_delete_event(event):
    repo_name = event["repo"]["name"]
    ref_type = event["payload"]["ref_type"]
    ref_name = event["payload"]["ref"]
    actor_name = event["actor"]["login"]
    print(f"- :wastebasket: {actor_name} deleted a {ref_type} '{ref_name}' in {repo_name}")

def print_fork_event(event):
    repo_name = event["repo"]["name"]
    forked_from = event["payload"]["forkee"]["full_name"]
    actor_name = event["actor"]["login"]
    print(f"- :fork_and_knife: {actor_name} forked {forked_from} to {repo_name}")

def print_member_event(event):
    repo_name = event["repo"]["name"]
    member_name = event["payload"]["member"]["login"]
    action = event["payload"]["action"]
    actor_name = event["actor"]["login"]
    print(f"- :family: {actor_name} {action} {member_name} to {repo_name}")

def print_publish_event(event):
    repo_name = event["repo"]["name"]
    actor_name = event["actor"]["login"]
    print(f"- :package: {actor_name} published a package in {repo_name}")

def print_unknown_event(event):
    print("Unknown event type. Event details:")
    print(event)

def print_event_details(event):
    event_type = event["type"]
    print(f"Event Type: {event_type}")
    print(f"Event Actor: {event['actor']['login']}")
    
    event_handlers = {
        "CommitCommentEvent": print_commit_comment_event,
        "PushEvent": print_push_event,
        "IssueCommentEvent": print_issue_comment_event,
        "IssuesEvent": print_issue_event,
        "PullRequestEvent": print_pull_request_event,
        "PullRequestReviewEvent": print_pull_request_review_event,
        "PullRequestReviewCommentEvent": print_pull_request_review_comment_event,
        "ReleaseEvent": print_release_event,
        "CreateEvent": print_create_event,
        "DeleteEvent": print_delete_event,
        "ForkEvent": print_fork_event,
        "MemberEvent": print_member_event,
        "PackageEvent": print_publish_event
    }

    handler = event_handlers.get(event_type, print_unknown_event)
    handler(event)