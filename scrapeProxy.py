import requests
import time
def scrapeProxy():
    links = []
    with open("proxy_sources.txt", "r") as file:
        for line in file.readlines():
            links.append(line.strip())
    file.close()

    lamount = len(links)
    print(f"[ ! ] Successfully loaded {lamount} links with HTTP/HTTP's proxy.")
    
    with open("proxy.txt", "w") as file:
        amount = 0
        for link in links:
            with requests.get(link) as request:
                if not request.ok:
                    print(f"[ - ] {link} returned {request.status_code}. Please check if this link is correct.")
                else:
                    file.write(f"{request.text}\n")

                    lines = len(request.text.split('\n'))
                    amount += lines
                    print(f"[ + ] {lines} lines appeared in proxy.txt")
    
    print(f"[ ! ] Finished with {amount} proxy's from {lamount} in proxy.txt!")
scrapeProxy()
