
def postback(i, user, tval):
    """Post a response based on the case number."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Get the function from the dictionary and call it if it exists
    func = result.get(i)
    return func() if func else None

# Example usage:
# postback(1, 'user123', '')  # This will send a message asking for the brand
