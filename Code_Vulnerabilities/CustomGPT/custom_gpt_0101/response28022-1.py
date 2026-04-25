
def postback(i, user, tval):
    """Function that posts a response to the database; message string must be less than 140 characters"""
    result = {
        1: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: postmarket(user, tval),
        3: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }
    return result.get(i, None)  # Return None if i is not in result

# Example usage
response = postback(1, "user123", "cream_type")
print(response)
