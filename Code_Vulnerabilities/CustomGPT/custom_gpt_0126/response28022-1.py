
def postback(i, user, tval):
    """Function that posts a response to the database; the message string must be less than 140 characters."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    return result.get(i, lambda: None)()  # Calls the function associated with the key, defaults to None if key not found.

# Example usage
# postback(1, 'user123', 'some_value')  # This will trigger the first case.
