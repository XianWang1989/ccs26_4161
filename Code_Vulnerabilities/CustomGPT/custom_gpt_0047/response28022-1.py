
def postback(i, user, tval):
    """Function that posts response to the database; message string must be less than 140 characters."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Call the function corresponding to the case, if it exists
    action = result.get(i)
    if action:
        return action()
    else:
        return None  # or handle an invalid case
