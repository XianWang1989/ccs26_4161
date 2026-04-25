
def postback(i, user, tval):
    """Function that posts a response to the database; the message string must be less than 140 characters."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Call the function if it exists
    func = result.get(i)
    if func:
        return func()
    else:
        return None  # or handle the case where i is not found
