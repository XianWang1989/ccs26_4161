
def postback(i, user, tval):
    """Function that posts a response to the database; the message string must be less than 140 characters."""

    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Get the corresponding function based on i and execute it
    action = result.get(i)
    if action:
        return action()  # Call the function if it's found
    else:
        return None  # Or handle the case where i is not found

# Example usage
postback(2, 'user123', 'smantana tip A')
