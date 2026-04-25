
def postback(i, user, tval):
    """Function to post a response; the message string must be less than 140 characters."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Call the corresponding lambda function if it exists
    return result.get(i, lambda: "Invalid option")()

# Example usage:
# response = postback(1, 'user123', 'some value')
# print(response)
