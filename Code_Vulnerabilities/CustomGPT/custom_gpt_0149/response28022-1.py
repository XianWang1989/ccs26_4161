
def postback(i, user, tval):
    """Function that posts a response based on the case number."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }
    # Call the function if it exists
    return result.get(i, lambda: None)()

# Example usage
response = postback(1, 'user123', 'some_tval')
print(response)
