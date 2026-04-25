
def postback(i, user, tval):
    """Function that returns a response based on the case number."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }
    return result.get(i, lambda: None)()  # Execute the function if it exists; return None if not.

# Example usage:
# response = postback(1, 'user123', 'some value')
