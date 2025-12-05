# import requests

# url = "https://webexapis.com/v1/rooms"

# payload = None

# headers = {
#     "Authorization": "Bearer YzhmMzRkNzItNWM4NC00ZDY4LWE3MTQtZTEzYmM4OGZiMDAyMWViMjc0OTAtZjVk_P0A1_5d96674f-de50-43d7-ae6b-8071b71cb457",
#     "Accept": "application/json"
# }

# response = requests.request('GET', url, headers=headers, data = payload)

# print(response.text.encode('utf8'))

import requests

url = "https://webexapis.com/v1/meetings"

payload = None

HEADERS = {
    "Authorization": "Bearer YzhmMzRkNzItNWM4NC00ZDY4LWE3MTQtZTEzYmM4OGZiMDAyMWViMjc0OTAtZjVk_P0A1_5d96674f-de50-43d7-ae6b-8071b71cb457",
    "Accept": "application/json;charset=UTF-8"
}

resp = requests.request('GET', url, headers=HEADERS, data = payload)

# print(response.text.encode('utf8'))
items=resp.json()["items"]
for item in items:
    print("Title:",item["title"],sep='\t')
    print("ID:",item["id"])
    meetingId=item["id"]
    print("Host:",item["hostDisplayName"],sep='\t')
    print("Web Link:",item["webLink"])
    print("Meeting Number: ",item["meetingNumber"])
    print("*"*20)

# url = 
# url = "https://webexapis.com/v1/meetings/"+meetingId+"/registrants"
url = "https://webexapis.com/v1/meetingParticipants?meetingId="+meetingId

resp=requests.get(url=url,headers=HEADERS)
# print(resp.text)
items=resp.json()["items"]
print("*"*40)
for reg in items:
    print("Name:",reg["displayName"])
    print("Email:",reg["email"])
    # print("First Name:",reg["firstName"])
    # print("Email Address: ",reg["email"])
    print("*"*20)
