import requests

def scrapeProxy():
    links = []
    with open("proxy_sources.txt", "r") as file:
        for line in file.readlines():
            links.append(line.strip())

    lamount = len(links)
    print(f"[ ! ] Successfully loaded {lamount} links with HTTP/HTTP's proxy.")

    with open("proxy.txt", "w") as file:
        amount = 0
        for link in links:
            response = requests.get(link)
            if not response.ok:
                print(f"[ - ] {link} returned {response.status_code}. Please check if this link is correct.")
            else:
                file.write(response.text + "\n")

                lines = len(response.text.split('\n'))
                amount += lines
                print(f"[ + ] {lines} lines appeared in proxy.txt")

    print(f"[ ! ] Finished with {amount} proxies from {lamount} in proxy.txt!")

scrapeProxy()
