
def postback(i, user, tval):
    """Function that posts a response to the database; message string must be less than 140 characters"""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    action = result.get(i)
    if action:
        return action()  # Call the function associated with the key

# Example usage
response = postback(1, 'john_doe', 'sour cream')
