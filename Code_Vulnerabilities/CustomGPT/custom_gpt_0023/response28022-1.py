
def postback(i, user, tval):
    """Function that posts a response; the message string must be less than 140 characters."""

    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Call the function if it exists for the given key `i`
    action = result.get(i)
    if action:
        return action()
    return None  # or some default response if `i` is not valid
