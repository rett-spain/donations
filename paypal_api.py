import requests
from requests.auth import HTTPBasicAuth


class PayPalAPI:
    #
    # Class constructor
    #
    def __init__(self, client_id, client_secret, base_url, token_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = base_url
        self.token_url = token_url
        self.access_token = None

    #
    # Get an access token from PayPal
    #
    def get_access_token(self):
        # Set the headers
        headers = {
            'Accept': 'application/json',
            'Accept-Language': 'en_US'
        }

        # Set the data for the request body
        data = {
            'grant_type': 'client_credentials'
        }

        response = requests.post(self.token_url,
                                 headers=headers,
                                 data=data,
                                 auth=HTTPBasicAuth(self.client_id, self.client_secret))
        if response.status_code == 200:
            self.access_token = response.json()['access_token']
            return self.access_token
        else:
            raise Exception('Failed to retrieve access token')

    #
    # List the transactions for a given date range
    #
    def list_transactions(self, start_date, end_date):
        # Set the URL for listing transactions
        url = self.base_url + '/v1/reporting/transactions'

        # Set the headers
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.access_token}'
        }
        # Set the parameters for the request
        params = {
            'fields': 'transaction_info,payer_info,shipping_info,auction_info,cart_info,incentive_info,store_info',
            'start_date': start_date,
            'end_date': end_date
        }

        # Make the get request to the API
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            transactions = response.json()['transaction_details']
            return transactions
        else:
            raise Exception('Failed to retrieve transactions')

    #
    # Print the transactions in a readable format
    #
    def print_transactions(self, transactions: list) -> None:
        for transaction in transactions:
            print(f'Full Name: {transaction["payer_info"]["payer_name"]["alternate_full_name"]}')
            print(f'Email Address: {transaction["payer_info"]["email_address"]}')
            print(f'Transaction Date: {transaction["transaction_info"]["transaction_initiation_date"]}')
            print(f'Transaction Amount: {transaction["transaction_info"]["transaction_amount"]["value"]} {transaction["transaction_info"]["transaction_amount"]["currency_code"]}')
            print(f'Transaction type: {transaction["transaction_info"]["transaction_event_code"]}')
            print('---')

    #
    # Print one transaction in a readable format
    #
    def print_transaction(self, transaction: dict) -> None:
        print(f'Full Name: {transaction["payer_info"]["payer_name"]["alternate_full_name"]}')
        print(f'Email Address: {transaction["payer_info"]["email_address"]}')
        print(f'Transaction Date: {transaction["transaction_info"]["transaction_initiation_date"]}')
        print(f'Transaction Amount: {transaction["transaction_info"]["transaction_amount"]["value"]} {transaction["transaction_info"]["transaction_amount"]["currency_code"]}')
        print(f'Transaction type: {transaction["transaction_info"]["transaction_event_code"]}')
