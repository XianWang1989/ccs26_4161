
def postback(i, user, tval):
    """Function that posts responses to the database; message string must be less than 140 characters."""

    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, f'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: {tval}')
    }

    # Call the function for the given case (if it exists)
    return result.get(i, lambda: None)()  # Default to None if i is not found

# Example usage
response = postback(1, 'user123', 'sour cream')
