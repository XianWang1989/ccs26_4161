
def postback(i, user, tval):
    """Function that posts a response based on input; message string must be less than 140 characters"""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }
    # Get the function based on the input and call it
    action = result.get(i)
    if action:  # Ensure that the action exists before calling it
        return action()  # Call the function
    else:
        return None  # Handle the case when 'i' is not found
