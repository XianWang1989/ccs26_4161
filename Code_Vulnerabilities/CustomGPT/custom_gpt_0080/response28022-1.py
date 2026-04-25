
def postback(i, user, tval):
    """Function that posts a response based on the input; the message must be less than 140 characters."""

    def case_1():
        return api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti')

    def case_2():
        return postmarket(user, tval)

    def case_3():
        return api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)

    result = {
        1: case_1,
        2: case_2,
        3: case_3
    }

    # Call the function if it exists, otherwise return None
    return result.get(i, lambda: None)()
