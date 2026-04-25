
def postback(i, user, tval):
    """Function that posts back a response; the message string should be less than 140 characters."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Call the function corresponding to the key i
    return result.get(i, lambda: None)()  # Returns None if i is not found

# Example usage:
# postback(1, 'user123', 'some_value')  # Should send the first message
