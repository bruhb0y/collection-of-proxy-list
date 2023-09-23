import requests
from datetime import datetime

generations = 10
params = {
    "api_key": "", # Put your API Key here. Create your account here: https://scrapeops.io/ to get it.
    "num_headers": "10" # If i know right, maximum amount of User Agents you can put here - 10.
}

print(f"[ {(datetime.now()).strftime('%H:%M:%S')} ] Starting generating {10*generations} user-agents...")
with open("agentUsers.txt", "w") as file:
    for i in range(generations):
        with requests.get("http://headers.scrapeops.io/v1/user-agents", params=params) as request:
            if not request.ok:
                print(f"[ {(datetime.now()).strftime('%H:%M:%S')} ] Error: {request.json()}"); break
            
            for user in (request.json())["result"]:
                file.write(f"{user}\n")
        print(f"[ {(datetime.now()).strftime('%H:%M:%S')} ] {generations-i} more generations left.")
