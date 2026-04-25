
def postback(i, user, tval):
    """Function to post a response to the database; the response string must be less than 140 characters."""

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

    # Call the function corresponding to the input `i`
    return result.get(i, lambda: "Invalid case")()

# Example usage
response = postback(1, 'user123', 'sour cream')
print(response)
