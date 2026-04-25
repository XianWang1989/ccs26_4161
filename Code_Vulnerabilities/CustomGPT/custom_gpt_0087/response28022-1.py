
def postback(i, user, tval):
    """Function that posts a response to the database; the message string must be less than 140 characters."""

    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Check if i is a valid key and call the corresponding function
    return result.get(i, lambda: None)()  # Default to a no-op if i is not found

# Example usage
# Assuming user and tval are predefined
postback(1, user, tval)
