
def postback(i, user, tval):
    """Function that posts a response to the database; the message string must be less than 140 characters."""

    def case1():
        return api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti')

    def case2():
        return postmarket(user, tval)

    def case3():
        return api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)

    result = {
        1: case1,
        2: case2,
        3: case3
    }

    return result.get(i, lambda: None)()  # default to None if i is not in the dictionary

# Example usage
response = postback(2, 'user123', 'tval_example')
print(response)
