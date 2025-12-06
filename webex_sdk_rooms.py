from webexteamssdk import WebexTeamsAPI #pip install webexteamssdk
from os import environ
from dotenv import load_dotenv #pip install python-dotenv

def get_env_var(env_var):
    return environ[env_var]

if __name__ == "__main__":
    load_dotenv()
    TOKEN=get_env_var("WEBEX_TEAMS_ACCESS_TOKEN")
    api = WebexTeamsAPI(access_token=TOKEN)
    print("=" * 20)
    rooms = api.rooms.list(max=50)
    room_count = 0
    for room in rooms:
        room_count += 1
        title = room.title if room.title else "No Title"
        print(f"{room.id[:5]} | {room.type[:10]} | {title[:20]}")
    print("=" * 20)
    print(f"\nRooms found: {room_count}")