
def postback(i, user, tval):
    """Function that posts the response based on the case provided."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Call the function associated with key 'i' if it exists in the dictionary
    return result.get(i, lambda: None)()  # Fallback to a no-op if the key doesn't exist
