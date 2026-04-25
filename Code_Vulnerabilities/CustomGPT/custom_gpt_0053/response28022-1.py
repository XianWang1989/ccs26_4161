
def postback(i, user, tval):
    """Posts a response to the database; the message string must be less than 140 characters."""

    # Define the actions to perform for each case
    actions = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Get the action based on i and call it if it exists
    action = actions.get(i)
    if action:
        return action()  # Call the action

# Example usage
# postback(1, "user123", "tval_example")
