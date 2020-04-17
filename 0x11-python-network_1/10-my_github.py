#!/usr/bin/python3
# takes your Github credentials (username and password)
# and uses the Github API to display your id
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(
            'https://api.github.com/user', auth=(argv[1], argv[2]))
    try:
        jfile = r.json()
        print(jfile['id'])
    except:
        print(None)
