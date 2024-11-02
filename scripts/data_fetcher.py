from api_fetcher import API_KEY

import requests

def fetch_data(symbol: str, function: str, params: dict) -> dict:
    """
    Fetch data from the Alpha Vantage API for a given symbol.

    Parameters:
    - symbol (str): The stock symbol for which to fetch data.
    - function (str): The type of data to fetch.
    - params (dict): Additional function parameters to pass to the API.

    Returns:
    - dict: Parsed JSON response from the API.
    """
    base_url = "https://www.alphavantage.co/query"
    params_api = {
        'function': function,
        'symbol': symbol,
        'apikey': API_KEY,
    }
    params_api.update(params)

    try:
        response = requests.get(base_url, params=params_api)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

        data = response.json()

        # Check if the API returned an error
        if "Error Message" in data:
            raise ValueError(f"API error: {data['Error Message']}")

        return data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return {}
    except ValueError as ve:
        print(ve)
        return {}


# Example usage
if __name__ == "__main__":

    symbol = "AAPL"  # Example stock symbol
    data = fetch_data(symbol, function = "TIME_SERIES_DAILY")

    from pprint import pprint
    pprint(data)