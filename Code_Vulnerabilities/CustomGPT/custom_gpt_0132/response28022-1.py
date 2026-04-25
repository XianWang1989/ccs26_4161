
def postmarket(user, tval):
    # Example implementation for postmarket (replace with actual code)
    return api.PostDirectMessage(user, f'Post market results for: {tval}')

def postback(i, user, tval):
    """Function that posts a response; message string must be less than 140 characters"""
    # Define actions as lambdas
    actions = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Call the appropriate action if it exists
    response = actions.get(i)
    if response:
        return response()  # Call the function stored in the dictionary

# Example usage
# postback(1, 'user123', 'some_value')
