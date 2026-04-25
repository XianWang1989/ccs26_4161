
def postback(i, user, tval):
    """Function that posts a message to the database; the string must be shorter than 140 characters"""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }
    return result.get(i, lambda: None)()  # Calls the lambda function if `i` exists, otherwise returns None

# Example usage:
response = postback(1, 'user123', 'sour cream')
print(response)
