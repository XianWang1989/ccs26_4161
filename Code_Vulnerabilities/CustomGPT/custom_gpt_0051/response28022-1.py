
def postback(i, user, tval):
    """Function that posts a response based on the case; 
       the message string must be under 140 characters."""

    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Call the function corresponding to the case, if it exists
    return result.get(i, lambda: None)()  # Default to a no-op if i is not found

# Example usage
# postback(1, 'username', 'some_value')
