import requests

def scrapeProxy():
    links = []
    proxys = []
    with open("proxy_sources.txt", "r") as file:
        for line in file.readlines():
            links.append(line.strip())

    lamount = len(links)
    print(f"[ ! ] Successfully loaded {lamount} links with HTTP/HTTP's proxy.")

    for link in links:
        amount = 0
        for link in links:
            response = requests.get(link)
            if response.ok:
                proxys.append(response.text)
                lines = len(response.text.split("\n"))
                print(f"[ + ] {lines} lines appeared in http_proxy.txt")

    with open("http_proxy.txt", "a") as file:
        for proxy in proxys:
            file.write(proxy)

    print(f"[ ! ] Finished with {amount} proxies from {lamount} in proxy.txt!")
scrapeProxy()
