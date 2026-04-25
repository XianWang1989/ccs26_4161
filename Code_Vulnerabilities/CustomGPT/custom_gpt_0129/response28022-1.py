
def postback(i, user, tval):
    """Function to post a response based on the input case"""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Call the function associated with the case if it exists
    action = result.get(i)
    if action:
        return action()  # Execute the function
    else:
        return None  # or handle the case where i is not found

# Example usage:
# Assuming api and postmarket are defined somewhere
# response = postback(1, 'user123', 'some_value')
