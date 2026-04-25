
def postback(i, user, tval):
    """Function that posts a response based on the input case."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    return result.get(i, lambda: 'Case not found')() # Call the function if found

# Example usage
# postback(1, 'user123', 'some_value')
