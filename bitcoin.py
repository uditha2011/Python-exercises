import json
import requests
import sys


try:
    if len(sys.argv) < 2:
        print("Missing command-line argument")
        sys.exit(1)

    elif len(sys.argv) == 2: #and sys.argv[1] is int:

        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        # print(json.dumps(response.json(), indent=2))

        o = response.json()

        for currency, info in o["bpi"].items():
            if currency == "USD":
                usd_rate_float = info["rate_float"]
                # print("USD Rate:", usd_rate_float)

        bitcoinrate = float(sys.argv[1]) * usd_rate_float
        print(f"${bitcoinrate:,.4f}")

        # usd_rate = data["bpi"]["USD"]["rate"]
        # print("USD Rate:", usd_rate)

    elif len(sys.argv) > 2:
        sys.exit()



except requests.RequestException as e:
    sys.exit(1)

except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)