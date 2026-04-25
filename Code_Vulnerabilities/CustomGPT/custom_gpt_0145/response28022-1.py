
def postback(i, user, tval):
    """Function that posts a response to the database; the message string must be less than 140 characters."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Call the appropriate function only if it exists in the dictionary
    if i in result:
        return result[i]()  # Call the lambda function
    else:
        return None  # Handle the case when i is not in the dictionary
