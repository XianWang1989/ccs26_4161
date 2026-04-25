
def postback(i, user, tval):
    """Function that returns a response based on index i; the message string must be less than 140 characters."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }
    # Get the function based on the index i and call it if it exists
    return result.get(i, lambda: "Invalid option")()

# Example usage
# Suppose user is 'test_user' and tval is 'sour cream'
# postback(1, 'test_user', 'sour cream') would send a message requesting the brand
# postback(2, 'test_user', 'sour cream') would call postmarket
# postback(3, 'test_user', 'sour cream') would send a message saying it doesn't know where to find it
# postback(4, 'test_user', 'sour cream') would return "Invalid option"
