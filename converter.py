# define a class that contains the app functionalities
import requests
import json
from Keys import key
import datetime


def list_currency():
    uri = "https://rapidapi.p.rapidapi.com/currencies"
    headers = {
        'x-rapidapi-host': "currencyscoop.p.rapidapi.com",
        'x-rapidapi-key': key
    }
    response = requests.request("GET", uri, headers=headers)
    json_response = json.loads(response.text)
    for values in json_response['response']['fiats'].values():
        print('Currency Name: ' + str(values['currency_name']) + ' | Currency Symbol: ' + str(values['currency_code']))


def parse_start_date():
    date_start = input('Enter start date (YYYY-MM-DD format):')
    year, month, day = map(int, date_start.split('-'))
    date = datetime.date(year, month, day)
    return date


def parse_end_date():
    date_end = input('Enter and end date (YYYY-MM-DD format):')
    year, month, day = map(int, date_end.split('-'))
    date = datetime.date(year, month, day)
    return date


def rate_converter(amount, base_currency, target_currency):
    uri = "https://rapidapi.p.rapidapi.com/query"
    query = {"function": "CURRENCY_EXCHANGE_RATE",
             "from_currency": base_currency,
             "to_currency": target_currency
             }
    headers = {
        'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
        'x-rapidapi-key': key
    }
    response = requests.request("GET", uri, headers=headers, params=query)
    json_response = json.loads(response.text)
    rate = float(json_response["Realtime Currency Exchange Rate"]['5. Exchange Rate'])
    converted = rate * amount
    return converted


def plot_currency(base_currency, target_currency):
    uri = "https://rapidapi.p.rapidapi.com/query"
    query = {"function": "FX_DAILY",
             "from_symbol": base_currency,
             "to_symbol": target_currency,
             "datatype": "json",
             "outputsize": "compact"
             }
    headers = {
        'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
        'x-rapidapi-key': key
    }

    response = requests.request("GET", uri, headers=headers, params=query)
    json_response = json.loads(response.text)
    for d in json_response["Time Series FX (Daily)"].values():
        print(d)
        value = d['4. close']
        print(value)


print(rate_converter(1, 'USD', 'BRL'))


plot_currency("USD", "CAD")


print(list_currency())