import requests
import sys
import json


url = "https://itunes.apple.com/search?entity=song&limit=50&term="
if len(sys.argv) != 2:
    sys.exit()

response = requests.get(url=url+sys.argv[1])
response = response.json()
for result in response['results']:
    print(result['trackName'])

