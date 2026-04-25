
def postback(i, user, tval):
    """Function that posts a response to the database; the string in the message must be less than 140 characters."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }
    return result.get(i, lambda: None)()  # Call the function if it exists, else return None

# Example usage:
# postback(1, 'some_user', 'some_value')
# postback(2, 'some_user', 'some_value')
# postback(3, 'some_user', 'some_value')
