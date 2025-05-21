'''
API references used in this code: https://api.artic.edu/docs/#collections

'''

import requests
import json

def main():
    print('Art Institute of Chicago!')
    artist = input('Artist: ')
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            params={'q': artist}
        )
        
        response.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete request!")
        return
    # content = json.dumps(response.json(),indent=2)
    content = response.json()
    for artwork in content['data']:
        print(f'* {artwork['title']}') 


main()