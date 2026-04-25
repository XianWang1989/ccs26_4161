
def postback(i, user, tval):
    """Function that posts the response to the database; the string in the message
    must be less than 140 characters."""

    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Call the function corresponding to the case. If i is not in result, return None.
    return result.get(i, lambda: None)()  # Call the function from the dictionary

# Example usage
# Assuming `api` and `postmarket` are defined elsewhere
# result = postback(2, 'user123', 'some value')
