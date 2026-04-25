
def postback(i, user, tval):
    """Function that posts a response to the database; the message string must be less than 140 characters"""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }
    # Execute only the function corresponding to the key i
    return result.get(i, lambda: None)()

# Example usage
# postback(1, 'user123', 'specific_value')  # Call with required parameters
