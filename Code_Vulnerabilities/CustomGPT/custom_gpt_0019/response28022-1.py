
def postback(i, user, tval):
    """Function that posts the response to the database; the string in the message must be less than 140 characters."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }
    # Execute the corresponding function if it exists
    return result.get(i, lambda: None)()  # Default to a no-op if i is out of range

# Example usage
# postback(1, 'user123', 'some_value')
