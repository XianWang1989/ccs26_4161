
def postback(i, user, tval):
    """Function that posts a response based on the input case; message length must be less than 140 characters."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Call the function associated with the key `i`.
    return result.get(i, lambda: None)()

# Example usage
# postback(1, 'username', 'tval_example')
