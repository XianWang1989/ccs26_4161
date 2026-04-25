
def postback(i, user, tval):
    """Posts a response based on the case number."""

    # Define the actions as functions
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Execute the function if the key exists
    return result.get(i, lambda: None)()  # Default to do nothing if key not found
