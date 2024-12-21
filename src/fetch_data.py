import requests
import pandas as pd
from datetime import datetime, timedelta


def fetch_crypto_data(crypto_ids, vs_currency='usd', days=30):
    """
    Fetch historical market data for cryptocurrencies using the CoinGecko API.

    Args:
        crypto_ids (list): List of cryptocurrency IDs (e.g., ['bitcoin', 'ethereum']).
        vs_currency (str): The currency to compare against (default: 'usd').
        days (int): Number of days of historical data.

    Returns:
        pd.DataFrame: DataFrame containing time series price data for each cryptocurrency.
    """
    base_url = "https://api.coingecko.com/api/v3/coins"
    all_data = []

    for crypto in crypto_ids:
        print(f"Fetching data for {crypto}...")
        url = f"{base_url}/{crypto}/market_chart"
        params = {'vs_currency': vs_currency, 'days': days}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            prices = response.json().get('prices', [])
            df = pd.DataFrame(prices, columns=['timestamp', crypto])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('timestamp', inplace=True)
            all_data.append(df)
        else:
            print(f"Failed to fetch data for {crypto}: {response.status_code}")

    if all_data:
        combined_df = pd.concat(all_data, axis=1)
        return combined_df
    else:
        return pd.DataFrame()


# Example usage:
cryptos = ['bitcoin', 'ethereum', 'binancecoin']
data = fetch_crypto_data(cryptos, days=30)
data.to_csv('C:/Users/Mohsen/Desktop/Desktop/AI/crypto-correlation-dashboard/data/crypto_prices.csv', index=True)
print("Data saved to 'C:/Users/Mohsen/Desktop/Desktop/AI/crypto-correlation-dashboard/data/crypto_prices.csv'")
