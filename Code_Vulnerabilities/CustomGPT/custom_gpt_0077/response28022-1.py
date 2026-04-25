
def postback(i, user, tval):
    """Function that posts response to the database; the message string should be less than 140 characters"""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Call the function associated with the provided index
    if i in result:
        return result[i]()  # Call the lambda to execute the function
    else:
        return None  # Or handle an invalid case as needed
