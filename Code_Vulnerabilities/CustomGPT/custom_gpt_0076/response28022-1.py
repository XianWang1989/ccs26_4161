
def postback(i, user, tval):
    """Function that posts a response; the message must be less than 140 characters."""

    def message_case_1():
        return api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti')

    def message_case_2():
        return postmarket(user, tval)

    def message_case_3():
        return api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)

    result = {
        1: message_case_1(),
        2: message_case_2(),
        3: message_case_3()
    }

    return result.get(i)

# Example usage:
# postback(1, 'user123', 'some_tval')
