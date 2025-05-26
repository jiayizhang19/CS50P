"""
In a file called bitcoin.py, implement a program that:

Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy. 

If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.

Queries the API for the CoinCap Bitcoin Price Index at rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey. 
You should replace YourApiKey with the actual API key you obtained from your CoinCap account dashboard, 
which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions.

Outputs the current cost of n Bitcoins in USD to four decimal places, using , as a thousands separator.

"""

import requests
import sys

url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=005824836522d341bc30e6d5720473c1dd31f122eb04894ea985655c6a7445ea"


def get_price():
    try:
        response = requests.get(url)
        price = response.json()["data"]["priceUsd"]
        return float(price)
    except requests.RequestException:
        pass


price = get_price()
if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
else:
    try:
        cost = float(sys.argv[1]) * price
    except ValueError:
        sys.exit("Command-line argument is not a number")
print(f"${cost:,.4f}")






