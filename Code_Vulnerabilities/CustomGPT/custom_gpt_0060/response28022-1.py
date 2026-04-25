
def postmarket(user, tval):
    # Example function for demonstration purposes
    return api.PostDirectMessage(user, 'Market response with value: %s' % tval)

def postback(i, user, tval):
    """Function to post a response based on the database; message string must be less than 140 characters"""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Execute the function if found
    response_func = result.get(i)
    return response_func() if response_func else None  # Call the function if it exists

# Example usage
# Assuming user is 'user123' and tval is 'some_value'
response = postback(1, 'user123', 'some_value')
print(response)
