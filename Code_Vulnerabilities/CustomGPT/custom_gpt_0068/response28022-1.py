
def postback(i, user, tval):
    """Function to post a response to the database; the message string must be less than 140 characters."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }
    # Call the function corresponding to the key 'i', if it exists
    return result.get(i, lambda: None)()  # Default to None if the key doesn't exist or call the selected lambda
