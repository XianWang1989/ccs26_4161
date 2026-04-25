
def postback(i, user, tval):
    """Function to post a response to the database; the message string must be less than 140 characters"""
    result = {
        1: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: postmarket(user, tval),
        3: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }
    # Use .get() to safely get the value, default to None if the key doesn't exist
    return result.get(i, 'Invalid option')

# Example usage:
response = postback(2, 'username', 'some_tval')
print(response)
