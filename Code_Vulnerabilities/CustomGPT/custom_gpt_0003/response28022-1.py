
def postback(i, user, tval):
    """This function posts a response to the database; the string in the message must be less than 140 characters."""

    # Define the response mappings
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, f'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: {tval}')
    }

    # Retrieve and execute the function corresponding to the key `i`
    # Use .get(i, lambda: None) to return None if the key doesn't exist
    return result.get(i, lambda: None)()

# Example usage:
# Assume `api` and `postmarket` are defined previously
# postback(1, 'user123', 'some_value')
