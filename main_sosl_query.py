from mysecrets import username, password, security_token
from salesforce_api import SalesForceAPI
from score_calc import calculate_relevance_score, print_results

# Obtain the access token from Salesforce
my_sf = SalesForceAPI(username, password, security_token)
my_sf.authenticate()

# Get the contact information by generic search
search_terms = input("Enter the generic info:")
results = my_sf.get_contactid_bygeneric(search_terms)

# Calculate the relevance score
for result in results['searchRecords']:
    relevance_score = calculate_relevance_score(search_terms, result)

    # Add the relevance score to the result as a new key-value pair
    result['relevance_score'] = relevance_score

# Sort the results based on the relevance score
results['searchRecords'].sort(key=lambda x: x['relevance_score'], reverse=True)

# Print just the top 5 results
print_results(results, 5)
