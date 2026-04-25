
def postback(i, user, tval):
    """Function that posts a response; the message string must be less than 140 characters"""

    # Define a dictionary with functions as values
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Call the function based on the value of i, if it exists
    return result.get(i, lambda: None)()  # Default to None if i is not in result
