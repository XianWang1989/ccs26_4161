
def postmarket(user, tval):
    # Example implementation of postmarket
    return api.PostDirectMessage(user, 'Searching in the market for: %s' % tval)

def postback(i, user, tval):
    """Function to post back response; the message string must be less than 140 characters"""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    action = result.get(i)
    if action:  # Check if there's a valid action
        return action()  # Call the function

    return None  # Return None if no valid case is found
