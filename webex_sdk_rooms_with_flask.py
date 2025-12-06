from webexteamssdk import WebexTeamsAPI #pip install webexteamssdk
from flask import Flask #pip install flask
from os import environ
from dotenv import load_dotenv #pip install python-dotenv

def get_env_var(env_var):
    return environ[env_var]

app=Flask(__name__)
@app.route('/')
def index():
   webex_rooms=get_rooms_info()
   return webex_rooms

def get_rooms_info():
    load_dotenv()
    TOKEN=get_env_var("WEBEX_TEAMS_ACCESS_TOKEN")
    api = WebexTeamsAPI(access_token=TOKEN)
    
    #build a list with rooms iformation
    rooms = []
    room_count=0
    webex_rooms = api.rooms.list()
    for room in webex_rooms:
        room_count+=1
        rooms.append({
            "id":room.id,
            "title":room.title,
            "type":room.type,
            "created":room.created
        })
    rooms.append({"room_count":room_count})
    return rooms

if __name__ == "__main__":

    app.run(debug=True,port=5000)

    
