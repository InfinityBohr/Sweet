import re
import certifi
import os
import requests


def runServers():
    with open("docs/playlist1.m3u8", "w") as file:
        file.write("#EXTM3U\n")
    for i in range(len(lis)):
        print(f"{i+1}.{lis[i]}")
        server1(i + 1, lis[i])
        
def server1(i, name):
    print("Running Server 1")
    url = f"http://cdntvpotok.com/sweet/{name}.php"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "http://sweet-tv.net/",
        "X-Requested-With": "XMLHttpRequest",
    }

    response = requests.get(url, headers=headers, verify=certifi.where())

    # Use regex to extract the source URL
    match = re.search(r'file:\s*"([^"]+playlist\.m3u8[^"]*)"', response.text)
    if match:
        stream_url = match.group(1)
        # print(stream_url)
        with open("docs/playlist1.m3u8", "a") as file:
            file.write(f"#EXTINF:-1,{name}\n")
            file.write(f"{stream_url}\n")

    else:
        print("No URL found.")



# For Server 1
print("Available Channels\nSome links might not works!!!")
lis = [
    "playboy",
    "hustlerhd",
    "hustler",
    "penthouse",
]

runServers() #Runs the function to start the servers!
