
def postback(i, user, tval):
    """Function that posts a response based on the input index."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval),
    }

    # Get the function based on input i and call it
    func = result.get(i)
    if func:
        return func()
    else:
        return None  # or some default action
