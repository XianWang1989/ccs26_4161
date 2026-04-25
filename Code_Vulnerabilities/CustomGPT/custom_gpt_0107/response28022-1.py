
def postback(i, user, tval):
    """Function that posts a response based on a case value."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }
    return result.get(i, lambda: None)()  # Call the function if it exists, else return None

# Example usage:
# postback(1, 'username', 'some_value')
