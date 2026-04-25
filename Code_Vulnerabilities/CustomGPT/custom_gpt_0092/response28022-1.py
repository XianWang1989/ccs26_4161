
def postback(i, user, tval):
    """Function that posts a response in the database; the message string must be less than 140 characters."""

    # Define the actions as functions (using lambdas for simplicity)
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Call the function based on input
    action = result.get(i)
    if action:
        return action()  # Execute the lambda function

    return None  # Handle the case if i is not in the dictionary
