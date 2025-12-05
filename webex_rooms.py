#imports
import requests #pip install requests
import json
from os import environ
from dotenv import load_dotenv #pip install python-dotenv

def get_env_var(env_var):
    return environ[env_var]

if __name__ == "__main__":
    load_dotenv()
    TOKEN=get_env_var("WEBEX_TEAMS_ACCESS_TOKEN")
    #"-de50-43d7-ae6b-8071b71cb457"

    print("*"*40)
    print(TOKEN)

#enumerate the rooms

#create the header to pass to the API call
HEADERS = {
    "Authorization": "Bearer "+TOKEN,
    "Accept": "application/json"
}

#create the API call
uri= "https://webexapis.com/v1/rooms"
resp=requests.get(uri,headers=HEADERS)

#evaluate the call
if resp.status_code != 200:
    print("Houston, we have a problem")
    print(resp.status_code)

#process the successful API call
else:
    room_counter=0
    room_menu={}
    items=resp.json()["items"]

    #print the rooms
    for item in items:
       room_counter+=1
       print(room_counter,item["title"],sep="\t") 
       room_menu[room_counter] = (item["id"],item["title"])

# get room id of the room of interest
room_num = int(input("Enter the menu option you wish to retrieve the list room members: "))
print(room_menu[room_num])
print("title:",room_menu[room_num][0])

#call the membership API
uri="https://webexapis.com/v1/memberships"

resp=requests.get(uri,headers=HEADERS)
if resp.status_code != 200:
    print("Houston, we have a problem")
    print(resp.status_code,"membership")
else:
    items=resp.json()["items"]

    #print the rooms
    room_members=0
    # for item in items:
    #    room_members+=1

    # #    print("Member Name: ",item["personDisplayName"],sep='\t')
    # #    print("Member Email Address: ",item["personEmail"],sep='\t')
    #    print("*"*40)
    print("*"*40)
    print(items)
    print("Member in room: ",room_members)

    #    print(room_counter,item["title"],sep="\t") 
    #    room_menu[room_counter] = (item["id"],item["title"])