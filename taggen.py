from multiprocessing.connection import wait
from time import sleep
import requests
import random
import json

pastebin = "https://pastebin.com/raw/zYEQvjcK"
r = requests.get(pastebin)
content = r.text
array = content.split(',')
list = array
def look(username):
    url = "https://api.twitter.com/graphql/P8ph10GzBbdMqWZxulqCfA/UserByScreenName?variables=%7B%22screen_name%22%3A%22" + username + "%22%2C%22withHighlightedLabel%22%3Atrue%7D"
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,bn;q=0.8",
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        "content-type": "application/json",
        "dnt": "1",
        'origin': 'https://twitter.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36',
        'x-twitter-active-user': 'yes',
        'x-twitter-client-language': 'en'
        }
    resp  = json.loads(requests.get(url, headers=headers).text)
    try:
        print(f"[N] {username} unavailable since " + resp["data"]["user"]["legacy"]["created_at"])
    except:
        try:
            err = resp["errors"][0]["message"]
            if "Not found" == err:
                print(f"[Y] {username} is available")
            else:
                print(f"[I] {username}, {err}")
        except:
            print(f"[Y] {username} is available.")
for i in range(1000):
    sleep(0.5)
    username = (''.join(random.sample(list, random.randint(2,2))))
    look(username)
