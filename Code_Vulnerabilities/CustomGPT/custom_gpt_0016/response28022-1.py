
def postback(i, user, tval):
    """Function that posts a response to the database; the string in the message must be less than 140 characters"""

    # Define a dictionary of functions that return responses based on the value of i
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Get the function and call it
    response_function = result.get(i)
    return response_function() if response_function else None

# Example usage
response = postback(1, 'user123', 'smantana')
print(response)
