from webexteamssdk import WebexTeamsAPI
from os import environ
from dotenv import load_dotenv #pip install python-dotenv

def get_env_var(env_var):
    return environ[env_var]

if __name__ == "__main__":
    load_dotenv()
    TOKEN=get_env_var("WEBEX_TEAMS_ACCESS_TOKEN")
    api = WebexTeamsAPI(access_token=TOKEN)
    print(f"{'Room ID (First 10 chars)':<25} | {'Type':<10} | {'Room Title'}")
    print("-" * 80)
    rooms = api.rooms.list(max=100)

    count = 0
    for room in rooms:
        count += 1
        # room.id is very long, so we slice it for cleaner display
        short_id = room.id[:20] + "..."
        room_type = room.type  # 'group' or 'direct'
        
        # Handle cases where 1-on-1 rooms might not have a distinct title
        title = room.title if room.title else "No Title (Direct Message)"

        print(f"{short_id:<25} | {room_type:<10} | {title}")

    print("-" * 80)
    print(f"\nTotal rooms found: {count}")