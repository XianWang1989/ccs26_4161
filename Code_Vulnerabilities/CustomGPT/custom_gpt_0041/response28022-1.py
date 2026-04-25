
def postback(i, user, tval):
    """functie ce posteaza raspunsul bazei de date; stringul din mesaj tb sa fie mai mic de 140 de caractere"""

    def case_1():
        return api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti')

    def case_2():
        return postmarket(user, tval)

    def case_3():
        return api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)

    # Dictionary of case functions
    result = {
        1: case_1,
        2: case_2,
        3: case_3
    }

    # Call the function associated with the provided case number
    return result.get(i, lambda: None)()  # Default to a no-op lambda if i is not found
