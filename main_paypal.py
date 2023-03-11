from mysecrets import paypal_client_id, paypal_client_secret, paypal_base_url, paypal_token_url
from paypal_api import PayPalAPI

# Create an instance of the PayPalAPI class and get an access token
my_paypal = PayPalAPI(paypal_client_id,
                      paypal_client_secret,
                      paypal_base_url,
                      paypal_token_url)
access_token = my_paypal.get_access_token()

# List the transactions for March 2023
transactions = my_paypal.list_transactions('2023-03-01T00:00:00Z', '2023-03-31T23:59:59Z')

# Print the transactions
my_paypal.print_transactions(transactions)
