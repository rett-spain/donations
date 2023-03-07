# Calculates the relevance score of a result based on the search terms
def calculate_relevance_score(text_input, result):
    # Split the search terms into a list
    search_terms = text_input.split()
    num_search_terms = len(search_terms)
    num_matching_terms = 0

    # Count the number of matching terms
    for term in search_terms:
        num_matching_terms += str(result).lower().count(term.lower())

    # Calculate the relevance score based on the number of matching terms
    relevance_score = num_matching_terms / num_search_terms

    # Add a bonus if the contact type is 'Socio ordinario' or 'Socio colaborador'
    if result['ContactType__c'] == 'Socio ordinario':
        relevance_score += 1
    elif result['ContactType__c'] == 'Socio colaborador':
        relevance_score += 0.5

    return relevance_score


# Function to print the results
def print_results(results, num_results=5):
    for result in results['searchRecords'][:num_results]:
        for field_name, field_value in result.items():
            if field_name != 'attributes':
                print(f"{field_name}: {field_value}")
        print()