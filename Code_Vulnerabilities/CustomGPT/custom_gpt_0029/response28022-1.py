
def postback(i, user, tval):
    """Function to post response to the database; the message string must be less than 140 characters"""

    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Call the function based on the case number
    return result.get(i, lambda: None)()  # Default to returning None if i is not in result

# Example usage:
# postback(1, 'user123', 'tval_example')
