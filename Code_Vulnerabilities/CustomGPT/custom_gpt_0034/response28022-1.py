
def postback(i, user, tval):
    """Posts a response based on the input case; the message string should be less than 140 characters."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }
    return result.get(i, lambda: None)()  # Call the function if found, else return None

# Example usage
postback(1, 'user123', 'tval_example')
