import sys
import requests

def get_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
        data = response.json()
        print(data['bpi']['USD']['rate'])
        return data['bpi']['USD']['rate']
    except (requests.RequestException, KeyError, ValueError):
        print('Error: Failed to retrieve Bitcoin price.')
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print('Missing command-line argument')
        sys.exit(1)

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        print('Error: Invalid number of Bitcoins specified.')
        sys.exit(1)

    bitcoin_price = get_bitcoin_price()
    total_cost = float(bitcoin_price.replace(',', '')) * bitcoins

    print(f'Total cost of {bitcoins:,.4f} Bitcoins: ${total_cost:,.4f}')

if __name__ == '__main__':
    main()
