
def postback(i, user, tval):
    """Function that posts a response to the database; the message string must be less than 140 characters"""
    # Define the actions as functions (lambdas or direct function references)
    actions = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Get the action based on 'i' and call it if it exists
    action = actions.get(i)
    if action:
        return action()  # Call the action (function)

# Example usage:
# Assuming api and postmarket are defined elsewhere in your code
# postback(1, 'user_id', 'some_value')
