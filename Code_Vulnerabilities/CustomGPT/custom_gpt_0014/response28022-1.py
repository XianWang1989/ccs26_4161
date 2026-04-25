
def postback(i, user, tval):
    """Function to post a response based on the input; the message must be less than 140 characters."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Call the function if it exists for the given key
    return result.get(i, lambda: None)()

# Example usage
response = postback(1, 'user123', 'some_value')
