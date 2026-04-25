
def postback(i, user, tval):
    """Function that posts a response to the database; the message string must be less than 140 characters."""

    # Define a dictionary with functions as values
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Call the function based on the key `i`
    return result.get(i, lambda: None)()  # Default to a no-op if i is not found

# Example usage
response = postback(1, 'username', 'some_value')
