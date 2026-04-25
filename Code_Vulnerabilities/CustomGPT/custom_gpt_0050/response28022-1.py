
def postback(i, user, tval):
    """Function that posts a response to the database; the message must be less than 140 characters."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Call the function associated with the case
    response = result.get(i)  # Get the lambda function
    if response:
        return response()  # Call the lambda to execute
    else:
        return None  # Handle case where 'i' is not valid

# Example usage
# postback(1, 'user123', 'some value')
