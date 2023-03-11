from mysecrets import paypal_client_id, paypal_client_secret, paypal_base_url, paypal_token_url, username, password, security_token
from paypal_api import PayPalAPI
from salesforce_api import SalesForceAPI


# Obtain the access token from Salesforce
my_sf = SalesForceAPI(username, password, security_token)
my_sf.authenticate()
print(my_sf.sf)

# Create an instance of the PayPalAPI class and get an access token
my_paypal = PayPalAPI(paypal_client_id,
                      paypal_client_secret,
                      paypal_base_url,
                      paypal_token_url)
access_token = my_paypal.get_access_token()

# List the transactions for all months in 2023
transactions_january = my_paypal.list_transactions('2023-01-01T00:00:00Z', '2023-01-31T23:59:59Z')
transactions_february = my_paypal.list_transactions('2023-02-01T00:00:00Z', '2023-02-28T23:59:59Z')
transactions_march = my_paypal.list_transactions('2023-03-01T00:00:00Z', '2023-03-31T23:59:59Z')

# Get all contact ids from Salesforce based on the emails in PayPal transactions
for transaction in transactions_january:
    # Get the contact id from Salesforce based on the email address
    contact_id = my_sf.get_contactid_byemail(transaction['payer_info']['email_address'])
    # Add the contact id to the transaction
    transaction['contact_id'] = contact_id

# Print the transactions
print("Printing the transactions with contact ids ***********")
for transaction in transactions_january:
    my_paypal.print_transaction(transaction)
    print(f'Transaction type: {transaction["contact_id"]}')
    print('---')
