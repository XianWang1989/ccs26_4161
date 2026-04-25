
def postback(i, user, tval):
    """Function that posts the response to the database; the message string must be shorter than 140 characters."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    return result.get(i, lambda: None)()  # calls the function if it exists

# Example usage
response = postback(1, 'user123', 'some_tval')  # Calls the first case
