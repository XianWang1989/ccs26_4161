
def postback(i, user, tval):
    """Function that posts the response to the database; the message string must be less than 140 characters"""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }
    # Execute the function for the corresponding case
    return result.get(i, lambda: None)()  # Provide a default case if `i` is not found

# Example of how to use the function
# postback(1, 'user123', 'some_tval')
